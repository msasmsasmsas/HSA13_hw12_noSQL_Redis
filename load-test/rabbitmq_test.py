import pika
import os
import time

# Получаем переменные окружения
RABBITMQ_USER = "admin"
RABBITMQ_PASS = "password"
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")  # <-- Теперь это передается через docker-compose.yml
QUEUE_NAME = "test_queue"

# Настройка соединения
credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
parameters = pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials)

# Подключение с попытками повторного подключения
max_retries = 10
for attempt in range(max_retries):
    try:
        print(f"Attempt {attempt + 1}: Connecting to RabbitMQ at {RABBITMQ_HOST}...")
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        print("Connected to RabbitMQ!")
        break
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Connection failed: {e}. Retrying in 5 seconds...")
        time.sleep(5)
else:
    print("Failed to connect to RabbitMQ after multiple attempts.")
    exit(1)

# Объявляем очередь
channel.queue_declare(queue=QUEUE_NAME, durable=True)
print(f"Queue '{QUEUE_NAME}' is ready. Waiting for messages...")

# Закрываем соединение
connection.close()
print("Connection closed.")

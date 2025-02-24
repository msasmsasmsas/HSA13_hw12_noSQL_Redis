import pika
import time

RABBITMQ_HOST = "rabbitmq"
QUEUE_NAME = "test_queue"

# Подключение к RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()

# Создаем очередь
channel.queue_declare(queue=QUEUE_NAME)

# Отправка сообщений
messages = 1000
sent_count = 0
error_count = 0

start_time = time.time()
for i in range(messages):
    try:
        message = f"Message {i}"
        channel.basic_publish(exchange="", routing_key=QUEUE_NAME, body=message)
        sent_count += 1
        print(f"Sent: {message}")
    except Exception as e:
        error_count += 1
        print(f"Error: {e}")

end_time = time.time()
elapsed_time = end_time - start_time

# Получение сообщений
received_count = 0
for method_frame, properties, body in channel.consume(QUEUE_NAME, inactivity_timeout=5):
    if method_frame:
        received_count += 1
        print(f"Received: {body.decode()}")
        channel.basic_ack(method_frame.delivery_tag)
    else:
        break

# Закрываем соединение
channel.close()
connection.close()

# Логирование результата
print(f"Total Sent: {sent_count}, Total Received: {received_count}, Errors: {error_count}")
print(f"Elapsed Time: {elapsed_time:.4f} seconds")

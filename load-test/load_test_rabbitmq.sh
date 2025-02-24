#!/bin/bash
set -e

echo "Running RabbitMQ Load Test..."

START_TIME=$(date +%s.%N)

# Количество сообщений
TOTAL_MESSAGES=1000

# Запуск теста
python3 /load-test/rabbitmq_test.py > output_rabbitmq.log

END_TIME=$(date +%s.%N)
TOTAL_TIME=$(echo "$END_TIME - $START_TIME" | bc)

# Парсим результаты
SUCCESS_COUNT=$(grep "Sent:" output_rabbitmq.log | wc -l)
FAIL_COUNT=$(grep "Error:" output_rabbitmq.log | wc -l)

# Записываем результат в JSON
echo "{
  \"transactions\": $TOTAL_MESSAGES,
  \"availability\": 100,
  \"elapsed_time\": $TOTAL_TIME,
  \"data_transferred\": 0,
  \"response_time\": $(echo "$TOTAL_TIME / $TOTAL_MESSAGES" | bc -l),
  \"transaction_rate\": $(echo "$TOTAL_MESSAGES / $TOTAL_TIME" | bc -l),
  \"throughput\": 0,
  \"concurrency\": 1,
  \"successful_transactions\": $SUCCESS_COUNT,
  \"failed_transactions\": $FAIL_COUNT,
  \"longest_transaction\": 0,
  \"shortest_transaction\": 0
}" | tee output_rabbitmq.json

echo "RabbitMQ Load Test completed."

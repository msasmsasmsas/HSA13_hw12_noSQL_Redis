#!/bin/bash
set -e

echo "Running Redis CLI Load Test (RDB)..."

START_TIME=$(date +%s.%N)

# Количество запросов
TOTAL_REQUESTS=1000

# Счетчики
SUCCESS_COUNT=0
FAIL_COUNT=0
LONGEST_TIME=0
SHORTEST_TIME=99999

# Запускаем тесты
for i in $(seq 1 $TOTAL_REQUESTS); do
    START=$(date +%s.%N)
    redis-cli -h redis-master -p 6379 SET "key_$i" "value_$i" > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
    else
        FAIL_COUNT=$((FAIL_COUNT + 1))
    fi
    END=$(date +%s.%N)

    ELAPSED=$(echo "$END - $START" | bc)
    if (( $(echo "$ELAPSED > $LONGEST_TIME" | bc -l) )); then
        LONGEST_TIME=$ELAPSED
    fi
    if (( $(echo "$ELAPSED < $SHORTEST_TIME" | bc -l) )); then
        SHORTEST_TIME=$ELAPSED
    fi
done

END_TIME=$(date +%s.%N)
TOTAL_TIME=$(echo "$END_TIME - $START_TIME" | bc)

# Вывод результатов в JSON
echo "{
  \"transactions\": $TOTAL_REQUESTS,
  \"availability\": 100,
  \"elapsed_time\": $TOTAL_TIME,
  \"data_transferred\": 0,
  \"response_time\": $(echo "$TOTAL_TIME / $TOTAL_REQUESTS" | bc -l),
  \"transaction_rate\": $(echo "$TOTAL_REQUESTS / $TOTAL_TIME" | bc -l),
  \"throughput\": 0,
  \"concurrency\": 1,
  \"successful_transactions\": $SUCCESS_COUNT,
  \"failed_transactions\": $FAIL_COUNT,
  \"longest_transaction\": $LONGEST_TIME,
  \"shortest_transaction\": $SHORTEST_TIME
}" | tee output_rdb.json

echo "Test completed for Redis RDB."

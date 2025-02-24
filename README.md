# HSA13_hw12_noSQL_Redis

hsa13-hw12-load-tester  | Running Redis CLI Load Test (RDB)...

hsa13-hw12-load-tester  | {

hsa13-hw12-load-tester  |   "transactions": 1000,

hsa13-hw12-load-tester  |   "availability": 100,

hsa13-hw12-load-tester  |   "elapsed_time": 8.806067484,

hsa13-hw12-load-tester  |   "data_transferred": 0,

hsa13-hw12-load-tester  |   "response_time": .00880606748400000000,

hsa13-hw12-load-tester  |   "transaction_rate": 113.55806684617498895378,

hsa13-hw12-load-tester  |   "throughput": 0,

hsa13-hw12-load-tester  |   "concurrency": 1,

hsa13-hw12-load-tester  |   "successful_transactions": 1000,

hsa13-hw12-load-tester  |   "failed_transactions": 0,

hsa13-hw12-load-tester  |   "longest_transaction": .022320312,

hsa13-hw12-load-tester  |   "shortest_transaction": .003829413

hsa13-hw12-load-tester  | }

hsa13-hw12-load-tester  | Test completed for Redis RDB.




hsa13-hw12-load-tester  | Running Redis CLI Load Test (AOF)...

hsa13-hw12-load-tester  | {

hsa13-hw12-load-tester  |   "transactions": 1000,

hsa13-hw12-load-tester  |   "availability": 100,

hsa13-hw12-load-tester  |   "elapsed_time": 9.071569749,

hsa13-hw12-load-tester  |   "data_transferred": 0,

hsa13-hw12-load-tester  |   "response_time": .00907156974900000000,

hsa13-hw12-load-tester  |   "transaction_rate": 110.23450490586091838249,

hsa13-hw12-load-tester  |   "throughput": 0,

hsa13-hw12-load-tester  |   "concurrency": 1,

hsa13-hw12-load-tester  |   "successful_transactions": 1000,

hsa13-hw12-load-tester  |   "failed_transactions": 0,

hsa13-hw12-load-tester  |   "longest_transaction": .013788809,

hsa13-hw12-load-tester  |   "shortest_transaction": .003754811

hsa13-hw12-load-tester  | }

hsa13-hw12-load-tester  | Test completed for Redis AOF.




hsa13-hw12-load-tester  | Running RabbitMQ Load Test...
rabbitmq                | 2025-02-24 23:41:32.564691+00:00 [info] <0.839.0> accepting AMQP connection <0.839.0> (172.18.0.8:45994 -> 172.18.0.3:5672)
rabbitmq                | 2025-02-24 23:41:32.567232+00:00 [info] <0.839.0> connection <0.839.0> (172.18.0.8:45994 -> 172.18.0.3:5672): user 'admin' authenticated and granted access to vhost '/'
rabbitmq                | 2025-02-24 23:41:32.575275+00:00 [info] <0.839.0> closing AMQP connection <0.839.0> (172.18.0.8:45994 -> 172.18.0.3:5672, vhost: '/', user: 'admin')
hsa13-hw12-load-tester  | {
hsa13-hw12-load-tester  |   "transactions": 1000,
hsa13-hw12-load-tester  |   "availability": 100,
hsa13-hw12-load-tester  |   "elapsed_time": .087518635,
hsa13-hw12-load-tester  |   "data_transferred": 0,
hsa13-hw12-load-tester  |   "response_time": .00008751863500000000,
hsa13-hw12-load-tester  |   "transaction_rate": 11426.13798764114636842770,
hsa13-hw12-load-tester  |   "throughput": 0,
hsa13-hw12-load-tester  |   "concurrency": 1,
hsa13-hw12-load-tester  |   "successful_transactions": 0,
hsa13-hw12-load-tester  |   "failed_transactions": 0,
hsa13-hw12-load-tester  |   "longest_transaction": 0,
hsa13-hw12-load-tester  |   "shortest_transaction": 0
hsa13-hw12-load-tester  | }
hsa13-hw12-load-tester  | RabbitMQ Load Test completed.



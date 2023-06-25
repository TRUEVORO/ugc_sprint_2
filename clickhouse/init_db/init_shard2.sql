CREATE DATABASE IF NOT EXISTS shard;
CREATE DATABASE IF NOT EXISTS replica;

CREATE TABLE IF NOT EXISTS shard.kafka_view
(
    user_id      String,
    film_id      String,
    viewed_frame Int16,
    event_time   DateTime('Europe/Moscow')
) ENGINE = Kafka
      SETTINGS kafka_broker_list = 'kafka:29092',
               kafka_topic_list = 'view',
               kafka_group_name = 'viewers-group',
               kafka_format = 'JSONEachRow',
               kafka_commit_every_batch = 1,
               kafka_num_consumers = 4,
               kafka_max_block_size = 1048576,
               kafka_poll_max_batch_size = 1048576,
               kafka_thread_per_consumer = 1,
               kafka_handle_error_mode = 'stream';


CREATE MATERIALIZED VIEW IF NOT EXISTS consumer TO shard.view
AS
SELECT *
FROM shard.kafka_view;

CREATE TABLE IF NOT EXISTS shard.view
(
    user_id      String,
    film_id      String,
    viewed_frame Int16,
    event_time   DateTime('Europe/Moscow')
) Engine=ReplicatedMergeTree('/clickhouse/tables/shard2/view', 'replica_1') PARTITION BY toYYYYMMDD(event_time) ORDER BY user_id;

CREATE TABLE IF NOT EXISTS replica.view
(
    user_id      String,
    film_id      String,
    viewed_frame Int16,
    event_time   DateTime('Europe/Moscow')
) Engine=ReplicatedMergeTree('/clickhouse/tables/shard1/view', 'replica_2') PARTITION BY toYYYYMMDD(event_time) ORDER BY user_id;

CREATE TABLE IF NOT EXISTS default.view
(
    user_id      String,
    film_id      String,
    viewed_frame Int16,
    event_time   DateTime('Europe/Moscow')
) ENGINE = Distributed('company_cluster', '', view, rand());

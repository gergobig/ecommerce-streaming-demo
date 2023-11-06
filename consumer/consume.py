import time
import json
import logging

from confluent_kafka import Consumer, KafkaException, KafkaError

from postgres.connector import PostgresConnector


MIN_COMMIT_COUNT = 10
CONF = {
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'ecommerce',
    'enable.auto.commit': 'false',
    'auto.offset.reset': 'earliest',
}


def main():
    # wait for cluster and producer to start
    time.sleep(60)
    consume_topic(['click','checkout'], process_events)


def process_events(message):
    row = json.loads(message.value())

    if 'event_type' not in row:
        raise ValueError('Required key (event_type) is missing!')

    with PostgresConnector() as conn:
        conn.insert(row, table=row['event_type'])


def consume_topic(topics: list, process_message_func):
    try:
        consumer = Consumer(CONF)
        consumer.subscribe(topics)

        message_count = 0
        while True:
            message = consumer.poll(timeout=1.0)
            if message is None:
                continue

            if message.error():
                if message.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    logging.error(
                        f'{message.topic()} [{message.partition()}] reached end at offset {message.offset()}\n'
                    )

                elif message.error():
                    raise KafkaException(message.error())
            else:
                process_message_func(message)
                message_count += 1
                if message_count % MIN_COMMIT_COUNT == 0:
                    consumer.commit(asynchronous=True)
                    logging.info('New offset is committed.')
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
    main()

import json
import time
import random
import logging

from confluent_kafka import Producer

from postgres.connector import PostgresConnector
from fake_data_generator.utils.args import get_args
from fake_data_generator.utils.generators import (
    generate_checkout_event,
    generate_click_event,
    generate_products,
    generate_users,
)

KAFKA_PRODUCER = Producer({'bootstrap.servers': 'kafka:9092'})


def main(no_users: int, no_products: int, no_events: int):
    users = generate_users(no_users)
    products = generate_products(no_products)

    with PostgresConnector() as conn:
        conn.insert_batch(users, 'users')
        conn.insert_batch(products, 'products')

    time.sleep(15)
    for _ in range(no_events):
        simulate_event(
            select_a_random_user(users, no_users), select_a_random_product(products, no_products)
        )


def select_a_random_user(users, no_users):
    return users[random.randint(0, no_users - 1)]


def select_a_random_product(products, no_products):
    return products[random.randint(0, no_products - 1)]


def produce_to_kafka(event, topic):
    def acked(err, msg):
        if err is not None:
            logging.info(f"Failed to deliver message: {str(msg)}: {str(err)}")

    KAFKA_PRODUCER.produce(topic, value=json.dumps(event).encode('utf-8'), callback=acked)
    KAFKA_PRODUCER.flush()


def simulate_event(user, product):
    # simulate click event 70% of the time
    if random.random() < 0.7:
        logging.info('Click generated')
        click = generate_click_event(user, product)
        produce_to_kafka(click, 'click')

    # simulate checkout event 30% of the time
    if random.random() < 0.3:
        logging.info('Checkout generated')
        checkout = generate_checkout_event(user, product)
        produce_to_kafka(checkout, 'checkout')


def wait_for_kafka():
    while True:
        try:
            KAFKA_PRODUCER.list_topics(timeout=5)
            break
        except Exception as e:
            logging.info(f'Waiting for Kafka to be ready... received message: "{e}"')
            time.sleep(5)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
    args = get_args()
    wait_for_kafka()
    main(args.no_users, args.no_products, args.no_events)

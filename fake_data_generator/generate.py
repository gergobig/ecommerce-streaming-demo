import random

from fake_data_generator.utils.connector import PostgresConnector
from fake_data_generator.utils.generators import (
    generate_checkout_event,
    generate_click_event,
    generate_products,
    generate_users,
)


def main(no_users: int, no_products: int, no_events: int):
    users = generate_users(no_users)
    products = generate_products(no_products)
    load_database(users, products)
    for _ in range(no_events):
        simulate_event(
            select_a_random_user(users, no_users), select_a_random_product(products, no_products)
        )


def select_a_random_user(users, no_users):
    return users[random.randint(0, no_users - 1)]


def select_a_random_product(products, no_products):
    return products[random.randint(0, no_products - 1)]


def load_database(users, products):
    with PostgresConnector() as conn:
        conn.insert_batch_data(users, 'users')
        conn.insert_batch_data(products, 'products')


def simulate_event(user, product):
    # simulate click event 70% of the time
    if random.random() < 0.7:
        click = generate_click_event(user, product)
        push_to_kafka(click)

    # simulate checkout event 30% of the time
    if random.random() < 0.3:
        checkout = generate_checkout_event(user, product)
        push_to_kafka(checkout)


def push_to_kafka(event):
    ...


if __name__ == '__main__':
    main(5, 10, 20)

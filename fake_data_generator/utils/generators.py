import uuid
import random
import datetime


import bcrypt
from faker import Faker
import faker_commerce

fake = Faker()
fake.add_provider(faker_commerce.Provider)


def generate_users(no_users: int):
    return [
        {
            'id': user_id,
            'username': fake.user_name(),
            'name': fake.name(),
            'password': bcrypt.hashpw(fake.password().encode('utf-8'), bcrypt.gensalt()),
        }
        for user_id in range(no_users)
    ]


def generate_products(no_products: int):
    return [
        {
            'id': product_id,
            'provider': fake.company(),
            'name': fake.ecommerce_name(),
            'category': fake.ecommerce_category(),
            'description': fake.text(),
            'price': round(fake.ecommerce_price(False) / 10000, 2),
        }
        for product_id in range(no_products)
    ]


def generate_click_event(user: dict, product: dict):
    click_event = {
        'id': str(uuid.uuid4()),
        'event_type': 'click',
        'user_id': user['id'],
        'product_id': product['id'],
        'url': fake.uri(),
        'ip_address': fake.ipv4(),
        'address': fake.address(),
        'event_timestamp': datetime.datetime.now(),
        'user_agent': fake.user_agent(),
    }

    return click_event


def generate_checkout_event(user: dict, product: dict):
    address = fake.address()

    checkout_event = {
        'id': str(uuid.uuid4()),
        'event_type': 'checkout',
        'user_id': user['id'],
        'product_id': product['id'],
        'payment_method': fake.credit_card_provider(),
        'total_amount': product['price'],
        'shipping_address': address,
        'billing_address': fake.address() if random.random() < 0.8 else address,
        'user_agent': fake.user_agent(),
        'ip_address': fake.ipv4(),
        'event_timestamp': datetime.datetime.now(),
    }

    return checkout_event

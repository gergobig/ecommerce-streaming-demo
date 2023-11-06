CREATE SCHEMA IF NOT EXISTS ecommerce;
SET SEARCH_PATH TO ecommerce;

CREATE TABLE IF NOT EXISTS ecommerce.users (
    id INT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS ecommerce.products (
    id INT PRIMARY KEY,
    provider VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    price DOUBLE PRECISION NOT NULL
);


CREATE TABLE IF NOT EXISTS ecommerce.click (
    id VARCHAR(255) PRIMARY KEY,
    event_type VARCHAR(255) NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    product_id VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    ip_address VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    event_timestamp VARCHAR(255) NOT NULL,
    user_agent VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS ecommerce.checkout (
    id VARCHAR(255) PRIMARY KEY,
    event_type VARCHAR(255) NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    product_id VARCHAR(255) NOT NULL,
    payment_method VARCHAR(255) NOT NULL,
    total_amount DOUBLE PRECISION NOT NULL,
    shipping_address VARCHAR(255) NOT NULL,
    billing_address VARCHAR(255) NOT NULL,
    user_agent VARCHAR(255) NOT NULL,
    ip_address VARCHAR(255) NOT NULL,
    event_timestamp VARCHAR(255) NOT NULL
);

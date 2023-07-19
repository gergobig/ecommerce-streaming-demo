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

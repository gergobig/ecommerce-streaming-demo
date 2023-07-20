# demo-de-project-streaming

## Project Description
This project demonstrates an ecommerce data generation system that utilizes Docker and Docker Compose to set up and orchestrate various services. It generates fake ecommerce data, stores it in a PostgreSQL database, and sends events like clicks and checkouts to Apache Kafka.

It also includes a Kafka UI to monitor Kafka messages.

## Prerequisites
- Docker and Docker Compose

## How to run
- Start Docker.
- run `make start`
- (optional) open `localhost:8080` to monitor kafka.
## Architecture
```plantuml
@startuml
actor "User" as user
component "Fake Data Generator" AS datagen <<python>>
database "ecommerce DB" AS db <<postgres>>
queue "Event receiver" AS kafka <<kafka>>
component "Kafka UI" AS kafka_ui

user -- datagen: Starts simulation
datagen - db : Stores users and products
datagen -- kafka : Sends events to kafka
kafka )-( kafka_ui : frontend of kafka

@enduml
```
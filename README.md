# E-commerce microservices production-grade pet project

## High level overview
A production-inspired distributed e-commerce pet project platform built with Python, RabbitMQ, Docker, and modern observability tooling.

The system follows an event-driven architecture where independent services collaborate to process customer orders asynchronously. 

Orders are submitted through a lightweight client interface and flow through a series of domain-specific services responsible for inventory reservation, payment processing, order orchestration, and customer notifications.

Services communicate exclusively through RabbitMQ events, enabling loose coupling, horizontal scalability, and fault isolation. Each service owns its data and business logic while participating in a larger workflow through asynchronous message exchanges.

## Flow
1. User signs in with a simple username to record orders under their name
1. Order submitted through interface
2. Check if items are available in inventory
   1. If they are proceed
   2. If not tell the user which item is not present in which quantity and have them change their order
3. After passing the inventory check, resgiter order in database for this user
4. Remove the chosen item from the inventory and adjust accordingly
   

## Technical goals

- Event-driven communication via RabbitMQ
- Service isolation and ownership boundaries
- Distributed tracing with OpenTelemetry
- Metrics collection with Prometheus
- Visualization with Grafana
- Structured logging
- Dockerized local environment
- Automated testing with pytest
- CI/CD with GitHub Actions
- Retry and dead-letter queue mechanisms
- Idempotent message processing


## UV set up
For this project I'm using uv as the python package manager.
### Setup
- In the root project directory `/ecommerce-proj` I run `uv init` which creates all the necessary uv-related files needed.
- In the root `pyproject.toml` file, I define which packages are local members in order to register them as local workspace packages.
- The `uv lock` lives at the root level since it covers the whole workspace.
- The `ecommerce-shared` package is defined locally from the `shared` local package in the workspace and not from pypi.
- Inside each service, there is a pyproject.toml file to register them in the uv workspace as local packages as define as well in the root `pyproject.toml` file under workspace memebers.
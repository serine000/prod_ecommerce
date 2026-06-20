# E-commerce microservices production-grade pet project

## High level overview
 A production-inspired distributed e-commerce platform built with Python, RabbitMQ, Docker, and modern observability tooling.

The system follows an event-driven architecture where independent services collaborate to process customer orders asynchronously. Orders are submitted through a lightweight client interface and flow through a series of domain-specific services responsible for inventory reservation, payment processing, order orchestration, and customer notifications.

Services communicate exclusively through RabbitMQ events, enabling loose coupling, horizontal scalability, and fault isolation. Each service owns its data and business logic while participating in a larger workflow through asynchronous message exchanges.

The platform incorporates production-grade engineering practices including distributed tracing, structured logging, metrics collection, automated testing, containerization, and CI/CD pipelines. Operational visibility is provided through OpenTelemetry, Prometheus, Grafana, and centralized log aggregation, allowing complete observability of requests as they traverse the system.


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
# reactive-microservices-with-kafka-python
Solutions to Koject's project Reactive Microservices with Kafka

## How to run the applications
0. Copy .env's
```bash
cp users/.env.example users/.env
cp profiles/.env.example profiles/.env
```
1. Spin up the containers
```bash
docker-compose up -d --build
```
2. Run database migrations
```bash
docker exec users-service poetry run alembic upgrade head
docker exec users-service poetry run alembic upgrade head
```
4. Check the API docs on http://localhost:8001/docs and http://localhost:8002/docs

# Comments Engine Api Python
Solution to Koject's Comments Engine API Project, trying to follow DDD principles and implementing an Hexagonal Architecture, using Python, FastAPI, Pydantic as main libraries, and PostgreSQL for persistence.

## How to run the service
1. Spin up the containers
```bash
docker-compose up -d --build
```
2. Run database migrations
```bash
docker exec comments-engine-backend poetry run alembic upgrade head
```
3. Run the tests
```bash
poetry run make tests
```
4. Check the API docs on http://localhost:8001/docs

## Other stuff
docker exec comments-engine-backend poetry run alembic revision --autogenerate
docker exec comments-engine-backend poetry run alembic upgrade head

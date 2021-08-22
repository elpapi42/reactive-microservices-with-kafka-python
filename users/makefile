start:
	uvicorn --host 0.0.0.0 --port 8000 source.shared.infrastructure.fastapi:app

start-development:
	uvicorn --host 0.0.0.0 --port 8000 --reload --reload-dir source source.shared.infrastructure.fastapi:app

test:
	pytest -s

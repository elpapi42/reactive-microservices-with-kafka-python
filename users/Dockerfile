FROM python:3.8.8
LABEL maintainer="Whitman Bohorquez"

RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install poetry

WORKDIR /application

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
RUN poetry install

RUN apt-get autoremove -y gcc

COPY . .

CMD ["poetry", "run", "make", "start"]

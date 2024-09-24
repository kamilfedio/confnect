FROM python:3.12-slim

ENV POETRY_VERSION=1.8.1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry==$POETRY_VERSION

RUN adduser --disabled-password --gecos '' celeryuser

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

COPY . /app

RUN chown -R celeryuser:celeryuser /app

USER celeryuser

EXPOSE 8000

CMD ["sh", "-c", "alembic upgrade head && uvicorn source.main:app --host 0.0.0.0 --port 8000"]


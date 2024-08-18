# Base image with Python 3.12
FROM python:3.12-slim

# Set environment variables
ENV POETRY_VERSION=1.8.1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Poetry
RUN pip install poetry==$POETRY_VERSION

# Create directory for the app
WORKDIR /app

# Copy pyproject.toml and poetry.lock to install dependencies
COPY pyproject.toml poetry.lock /app/

# Install dependencies with Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copy the rest of the application code
COPY . /app

# Expose the application port
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn
CMD ["sh", "-c", "alembic upgrade head && uvicorn source.main:app --host 0.0.0.0 --port 8000 --reload"]


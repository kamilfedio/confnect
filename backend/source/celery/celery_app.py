from celery import Celery

from source.config.env_config import redis_config

# celery config
celery = Celery(
    "worker",
    broker=redis_config.REDIS_URL,
    backend=redis_config.REDIS_URL,
    broker_connection_retry_on_startup=True,
)

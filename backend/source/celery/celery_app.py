from celery import Celery

from source.config.env_config import redis_config

# celery config
celery: Celery = Celery(
    "tasks",
    broker=redis_config.REDIS_URL,
    backend=redis_config.REDIS_URL,
    broker_connection_retry_on_startup=True,
)

celery.autodiscover_tasks(["source.celery.tasks"])

celery.conf.update(
    timezone="UTC",
    enable_utc=True,
)

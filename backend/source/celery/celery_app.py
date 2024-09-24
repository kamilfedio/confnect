import json
from celery import Celery
from celery.schedules import timedelta
from asgiref.sync import async_to_sync

from source.utils.emails import send_email
from source.config.env_config import redis_config

# celery config
celery: Celery = Celery(
    "worker",
    broker=redis_config.REDIS_URL,
    backend=redis_config.REDIS_URL,
    broker_connection_retry_on_startup=True,
)

celery.autodiscover_tasks(['source.celery.tasks'])

# schedule tasks
celery.conf.beat_schedule = {
    "delete_expirated_tokens": {
        "task": "source.celery.tasks.delete_expirated_tokens",
        "schedule": timedelta(minutes=1),
    }
}

celery.conf.timezone = "UTC"

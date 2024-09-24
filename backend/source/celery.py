from celery import Celery
from asgiref.sync import async_to_sync
import json

from source.config.env_config import redis_config
from source.utils.emails import send_email

celery = Celery(
    "worker",
    broker=redis_config.REDIS_URL,
    backend=redis_config.REDIS_URL,
    broker_connection_retry_on_startup=True,
)


@celery.task
def send_email_queue(email_schema_str: str) -> None:
    email_schema_dict: dict = json.loads(email_schema_str)
    async_to_sync(send_email)(email_schema_dict)

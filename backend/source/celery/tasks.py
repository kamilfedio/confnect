from asgiref.sync import async_to_sync
import json

from backend.source.celery import celery_app
from source.utils.emails import send_email


@celery_app.task
def send_email_queue(email_schema_str: str) -> None:
    """
    send email in queue
        email_schema_str (str): email schema
    """
    email_schema_dict: dict = json.loads(email_schema_str)
    async_to_sync(send_email)(email_schema_dict)

from asgiref.sync import async_to_sync
import json

from source.database import get_async_session
from source.crud.tokens import delete_expirated
from source.utils.emails import send_email
from source.celery.celery_app import celery


@celery.task
def send_email_queue(email_schema_str: str) -> None:
    """
    send email in queue
        email_schema_str (str): email schema
    """
    email_schema_dict: dict = json.loads(email_schema_str)
    async_to_sync(send_email)(email_schema_dict)

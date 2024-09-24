from email.message import EmailMessage
import smtplib
from jinja2 import Environment, FileSystemLoader, Template

from source.schemas.utils import EmailSchema
from source.config.env_config import email_config
from source.utils.enums import EmailType
from source.config.config import config

env = Environment(loader=FileSystemLoader("source/templates"))


def _render_template(template_name: str, context: dict[str, str]) -> str:
    """
    render the jinja2 templates
    Args:
        template_name (str): template file name
        context (dict): data

    Returns:
        str: rendered template
    """
    template: Template = env.get_template(template_name)
    return template.render(context)


def send_email(email_schema: EmailSchema) -> None:
    """
    send email to user
    Args:
        email_schema (EmailSchema): email schema data
    """
    match email_schema.type:
        case EmailType.RESET_PASSWORD:
            content: str = _render_template("reset_password.html", email_schema.content)
        case _:
            raise ValueError("Invalid email type")

    email = EmailMessage()
    email["from"] = config.title
    email["to"] = email_schema.to
    email["subject"] = email_schema.subject
    email.set_content(content, subtype="html")
    with smtplib.SMTP(
        host=email_config.EMAIL_SERVER, port=email_config.EMAIL_PORT
    ) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(user=email_config.EMAIL, password=email_config.EMAIL_PASSWORD)
        smtp.send_message(email)

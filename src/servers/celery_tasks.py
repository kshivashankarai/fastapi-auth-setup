from celery import Celery
from src.mails.mail import mail, create_message
from asgiref.sync import async_to_sync

# Initialize the Celery application.
c_app = Celery()

# Load the Celery configuration from the specified configuration file/module.
c_app.config_from_object("src.settings.config")


@c_app.task()
def send_email(recipients: list[str], subject: str, body: str):
    """
    A Celery task to send an email asynchronously.

    This function creates an email message and sends it using the mail object.
    The sending process is performed asynchronously by converting the async function
    into a synchronous call using async_to_sync.

    :param recipients: A list of recipient email addresses.
    :param subject: The subject of the email.
    :param body: The body content of the email.
    """
    # Create the email message with the given recipients, subject, and body.
    message = create_message(recipients=recipients, subject=subject, body=body)

    # Send the email message asynchronously, converting the async call to sync.
    async_to_sync(mail.send_message)(message)

    # Log that the email was sent.
    print("Email sent")

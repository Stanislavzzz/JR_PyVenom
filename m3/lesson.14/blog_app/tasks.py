from celery import shared_task
import time
from django.core.mail import send_mail


@shared_task
def add_task(x, y):
    time.sleep(5)
    return x + y


@shared_task
def send_email_task(recipient_email, subject, message):
    """Фоновая задача для отправки электронной почты."""
    send_mail(
        subject=subject,
        message=message,
        from_email='admin@example.com',
        recipient_list=[recipient_email],
    )
    return f"Email был отправлен {recipient_email}"

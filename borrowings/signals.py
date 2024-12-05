from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Borrowing
from utils.telegram_helper import send_telegram_message


@receiver(post_save, sender=Borrowing)
def send_notification(sender, instance, created, **kwargs) -> None:
    """Sends a notification in Telegram when a new Borrowing is created."""
    if created:
        message = (
            f"A new borrowing has been created for {instance.book.title} "
            f"on {instance.borrow_date}.\n"
            f"Expected return date is {instance.expected_return_date}."
        )
        send_telegram_message(message)

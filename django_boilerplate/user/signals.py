from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_boilerplate.user.models import User
from django_boilerplate.user.tasks import send_greeting_email


@receiver(post_save, sender=User)
def greet_user(sender, instance: User, created, **kwargs):
    if created and instance.email is not None:
        transaction.on_commit(lambda: send_greeting_email(instance.pk))

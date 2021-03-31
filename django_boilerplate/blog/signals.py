from django.db.models.signals import post_delete
from django.dispatch import receiver

from django_boilerplate.blog.models import BackgroundImage


@receiver(post_delete, sender=BackgroundImage)
def shitty_signal(sender, instance: BackgroundImage, **kwargs):
    raise RuntimeError()

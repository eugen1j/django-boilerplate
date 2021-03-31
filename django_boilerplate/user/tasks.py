import dramatiq
from django.core.mail import send_mail
from django.utils import timezone
from periodiq import cron
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from django.utils.translation import gettext_lazy as _

from django_boilerplate.settings import EMAIL_HOST_USER
from django_boilerplate.user.models import User


@dramatiq.actor(periodic=cron("@daily"))
def flush_expired_tokens():
    OutstandingToken.objects.filter(expires_at__lte=timezone.now()).delete()


@dramatiq.actor()
def send_greeting_email(user_id: int):
    user = User.objects.get(pk=user_id)

    if user.email is None:
        raise RuntimeError("User has no email")

    send_mail(
        subject=_("Welcome to Django Boilerplate!"),
        message=_("Some greetings!"),
        from_email=EMAIL_HOST_USER,
        recipient_list=[user.email],
    )

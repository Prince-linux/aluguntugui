from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from .models import QueuedEmail

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_activation(sender, instance, created, **kwargs):
    if created:
        user = instance
        data = {
            'host': settings.HOST,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        }
        QueuedEmail.objects.create(user=user,
                                   subject='Activate your account',
                                   template='emailer/activation_email.html',
                                   data=data)

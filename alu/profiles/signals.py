from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import update_last_login
from django.dispatch import receiver
from django.conf import settings
from .models import Profile, Timeline

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(user_logged_in)
def check_first_login(sender, user, **kwargs):
    if user.last_login is None:
        Timeline.objects.create(user=user, activity='First login')
    update_last_login(sender, user, **kwargs)

user_logged_in.disconnect(update_last_login, dispatch_uid='update_last_login')

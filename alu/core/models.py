from django.db import models
from django.conf import settings
import django.utils.timezone as tz
    
class Activation(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True)
    
    def __str__(self):
        return "{}".format(self.user.email)

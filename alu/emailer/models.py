from django.db import models
from django.conf import settings
import django.utils.timezone as tz

class QueuedEmail(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    data = models.JSONField(null=True)

    def __str__(self):
        return "{}".format(self.user.email)


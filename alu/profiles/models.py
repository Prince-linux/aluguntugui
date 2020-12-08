from datetime import datetime, timedelta
from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')

    def __str__(self):
        return self.user.username

class TimelineManager(models.Manager):
    def get_user_timeline(self, user, days=7):
        # TODO: date format should be configurable
        today = datetime.now()
        first = today - timedelta(days=days)
        dr = [d for d in (today - timedelta(days=n) for n in range(days))]
        timeline = {d.strftime("%Y-%m-%d"): [] for d in dr}
        for item in Timeline.objects.filter(user=user, timestamp__gte=first):
            d = item.timestamp.strftime("%Y-%m-%d")
            timeline[d].append(item.activity)
        return timeline
        
class Timeline(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='timeline')
    activity = models.TextField()

    objects = TimelineManager()
    
    class Meta:
        ordering = ['-timestamp']

from django.db import models
from django.utils import timezone


class MetarData(models.Model):
    data = models.JSONField()
    timestamp = models.DateTimeField(default=timezone.now)

    def is_cache_expired(self):
        return timezone.now() > self.timestamp + timezone.timedelta(minutes=5)

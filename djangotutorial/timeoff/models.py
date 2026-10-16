import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Timeoff(models.Model):
    reason = models.CharField("Reason for leave", max_length=200)
    pub_date = models.DateTimeField("date published")
    leave_date = models.DateTimeField()
    return_date = models.DateTimeField()
    
    def __str__(self):
        return self.reason
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
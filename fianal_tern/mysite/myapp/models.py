# Create your models here.
from django.db import models
from django.utils import timezone
class myapp(models.Model):
    thing_name = models.CharField(max_length = 20)#事件名上限20字
    thing_time = models.DateTimeField(default=timezone.now)#預設現在
    thing_where =models.CharField(max_length = 20)#地點名上限20字


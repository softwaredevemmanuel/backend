from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, timedelta
import secrets



# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

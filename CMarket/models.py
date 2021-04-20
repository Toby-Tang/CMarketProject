from django.db import models

# the following lines added:
import datetime
from django.utils import timezone


class Post(models.Model):
    content = models.CharField(max_length=4000)
    origin = models.CharField(max_length=30)


class Message(models.Model):
    target = models.CharField(max_length=30)
    content = models.CharField(max_length=4000)
    origin = models.CharField(max_length=30)

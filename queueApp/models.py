from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Queue(models.Model):
    name = models.CharField(max_length=100)
    admins = models.ManyToManyField(User)
    timestamp = models.DateTimeField(auto_now_add=True)


class QueuePlace(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    place = models.TextField()
    queue = models.ForeignKey('Queue', on_delete=models.CASCADE)

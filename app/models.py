from django.db import models
from datetime import datetime


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now)
    body = models.TextField()
    # media ?

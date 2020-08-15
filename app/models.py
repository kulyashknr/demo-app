from django.db import models
from datetime import datetime
from utils.upload import article_pic_path
from utils.validators import validate_file_size


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now)
    body = models.TextField()
    picture = models.ImageField(upload_to=article_pic_path, validators=[validate_file_size], blank=True, null=True)

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class BlogPost(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=400)
    date = models.CharField(max_length=30)
    body = RichTextField()
    img_url = models.URLField()

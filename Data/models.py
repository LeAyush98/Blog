from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

def get_default_user() -> User:
    me = User.objects.get(username = "ayush")
    return me.id

# Create your models here.
class BlogPost(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=400)
    date = models.CharField(max_length=30)
    body = RichTextField()
    img_url = models.URLField()  
    user = models.ForeignKey(to=User, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Comments(models.Model):
    comment = models.CharField(max_length=400)
    user = models.ForeignKey(to= User, on_delete= models.CASCADE)
    blog_post = models.ForeignKey(to= BlogPost, on_delete= models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.user}'s comment on {self.blog_post}"
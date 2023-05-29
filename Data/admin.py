from django.contrib import admin
from .models import BlogPost, Comments

# Register your models here.
class BlogPostPresence(admin.ModelAdmin):
    model = BlogPost
    fields = ["author", "title", "subtitle", "date", "body", "img_url", "user"]

class CommentsPresence(admin.ModelAdmin):
    model = Comments
    fields = ["comment", "user", "blog_post"]

admin.site.register(BlogPost, BlogPostPresence)
admin.site.register(Comments, CommentsPresence)    
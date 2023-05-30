from django import forms
from .models import BlogPost, Comments

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "subtitle", "body", "img_url"]

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["comment"]        
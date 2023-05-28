from django.shortcuts import render
from .forms import BlogPostForm
from .models import BlogPost

# Create your views here.
def create_post(request):
    form = BlogPostForm()
    return render(request, "Data/create_post.html", {"form" : form})
from django.shortcuts import render
from .forms import BlogPostForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_post(request):
    form = BlogPostForm()
    return render(request, "Data/create_post.html", {"form" : form})
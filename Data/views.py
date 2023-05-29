from django.shortcuts import render
from .forms import BlogPostForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required
import datetime

def get_date() -> str:
    now = datetime.datetime.now()
    now = now.strftime("%B %d, %Y")
    return str(now)

# Create your views here.

@login_required
def create_post(request):
    form = BlogPostForm()
    
    return render(request, "Data/create_post.html", {"form" : form})
from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime

def get_date() -> str:
    now = datetime.datetime.now()
    now = now.strftime("%B %d, %Y")
    return str(now)

# Create your views here.

@login_required
def create_post(request):
    form = BlogPostForm()
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            BlogPost.objects.create(
                author = request.user.first_name.title(),
                title = form.cleaned_data["title"],
                subtitle = form.cleaned_data["subtitle"],
                date = get_date(),
                body = form.cleaned_data["body"],
                img_url = form.cleaned_data["img_url"],
                user = request.user
            )
            messages.success(request, "Post added successfully!")
            return redirect("home")
    set = BlogPost.objects.get(id=1)
    set.date = "September 16, 2020"
    set.save()
    sett = BlogPost.objects.get(id=2)
    sett.date = "November 4, 2021"
    sett.save()
    return render(request, "Data/create_post.html", {"form" : form})
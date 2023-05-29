from django.shortcuts import render, redirect
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
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            print(request.user.first_name)
            print(form.cleaned_data["title"])
            print(form.cleaned_data['subtitle'])
            print(form.cleaned_data["body"])
            print(form.cleaned_data['img_url'])
            print(get_date())
            return redirect("home")

    return render(request, "Data/create_post.html", {"form" : form})
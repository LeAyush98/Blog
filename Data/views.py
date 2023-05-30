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
    return render(request, "Data/create_post.html", {"form" : form})

@login_required
def update_post(request, id):
    post = BlogPost.objects.get(id = id)
    form = BlogPostForm(instance= post)
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.subtitle = form.cleaned_data['subtitle']
            post.body = form.cleaned_data['body']
            post.img_url = form.cleaned_data['img_url']
            post.save()
            messages.success(request, f"{post.author}'s post has been updated.")
            return redirect("home")

    if request.user.id == 1 or request.user.id == post.user_id:
        return render(request, "Data/edit_post.html", {"form" : form})
    else:
        messages.error(request, "You are not authorised to do that.")
        return redirect("home")

@login_required    
def delete_post(request, id):
    post = BlogPost.objects.get(id = id)
    if request.user.id == 1 or request.user.id == post.user_id:
        post.delete()
        messages.success(request, "Post successfully deleted.")
        return redirect("home")
    else:
        messages.error(request, "You are not authorised to do that.")
        return redirect("home")
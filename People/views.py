from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterUserForm

# Create your views here.

def register_user(request):
    form = RegisterUserForm()
    return render(request, "People/register.html", {"form" : form})

def login_user(request):
    if request.method == "POST":
        user = authenticate(request, username = request.POST["username"], password = request.POST["password"])
        if user:
            messages.success(request, f"Welcome {user}")
            return redirect("home")
        else:
            messages.success(request, f"Please check your credentials.")
            return redirect("login")
     
    return render(request, "People/login.html", {})
    
def logout_user(request):
    logout(request) 
    messages.success(request , (f"Log Out Successful! Hope to see you again!"))   
    return redirect('home')    

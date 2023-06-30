from django.shortcuts import render, redirect
from django.contrib import messages
from Data.models import BlogPost
import smtplib
import boto3
import os
from dotenv import load_dotenv

load_dotenv(".env")

AWS_REGION = "ap-south-1"
ssm_client = boto3.client("ssm", region_name=AWS_REGION)

def mail(name:str, email:str, message:str) -> None:
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=email,
        to_addrs=EMAIL,
        msg=f"Subject:Hello!\n\n{message}\n\nThanks and regards,\n{name}"
    )
    connection.close()

def contact(request):
    if request.method == "POST":
        messages.success(request, "Message sent")
        mail(request.POST["name"], request.POST["email"], request.POST["message"])
        return redirect("home")

# Create your views here.
def home(request):
    contact(request)
    posts = BlogPost.objects.all().order_by("id")
    return render(request, "Main/index.html", {"posts" : posts})

def about(request):
    contact(request)
    return render(request, "Main/about.html", {})
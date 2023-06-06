from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BlogPost, Comments
import smtplib
import boto3
import os

AWS_REGION = "ap-south-1"
ssm_client = boto3.client("ssm", region_name=AWS_REGION)

def mail(author:str, title:str) -> None:
    EMAIL = ssm_client.get_parameter(Name='contact_email', WithDecryption=True)['Parameter']['Value']
    PASSWORD = ssm_client.get_parameter(Name='contact_password', WithDecryption=True)['Parameter']['Value']

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg=f"Subject:New Post!\n\n{author.title()} has added a new post today, title is: {title}.\n\nThanks and regards,\nBlog Manager"
    )
    connection.close()

def notifier(sender, instance, created, **kw):
    if created:
        mail(instance.author, instance.title)

post_save.connect(receiver= notifier, sender= BlogPost)    

# Alternate way with decorator 
# @receiver(signal= post_save, sender = notifier)
# def notifier(sender, instance, created, **kw):
#     if created:
#         mail(instance.author, instance.title)
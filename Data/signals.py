from django.db.models.signals import post_save
from .models import BlogPost, Comments
import smtplib
from dotenv import load_dotenv
import os

load_dotenv(".env")

def mail(author:str, title:str) -> None:
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")

    connection = smtplib.SMTP("smtp.gmail.com")
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
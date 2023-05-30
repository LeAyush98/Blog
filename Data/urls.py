from django.urls import path
from .views import create_post, update_post, delete_post

urlpatterns = [
    path("create/", create_post, name="create"),
    path("update/<int:id>", update_post, name="update"),
    path("delete/<int:id>", delete_post, name= "delete")
]

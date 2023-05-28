from django.urls import path, include
from .views import login_user, logout_user, register_user

urlpatterns = [
    path("accounts/", include('allauth.urls')),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", register_user, name="register"),

]

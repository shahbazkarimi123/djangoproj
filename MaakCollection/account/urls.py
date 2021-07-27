from django.urls import path
from account import views

urlpatterns = [
    path("", views.base, name="base"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout1, name="logout"),
]

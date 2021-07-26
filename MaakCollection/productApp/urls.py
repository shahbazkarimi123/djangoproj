from django.urls import path
from productApp import views

urlpatterns = [
    path("", views.product, name="product"),
]
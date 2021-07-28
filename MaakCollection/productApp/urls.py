from django.urls import path
from productApp import views

urlpatterns = [
    path("create/", views.create, name="create"),
    path("product/", views.detail, name="products"), 
    

]
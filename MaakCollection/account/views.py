from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request, 'account/base.html')


def login(request):
    
    return render(request, 'account/login.html')

def signin(request):
    i
    return render(request, 'account/signin.html')
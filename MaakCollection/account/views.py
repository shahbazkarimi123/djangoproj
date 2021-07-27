from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def base(request):
    return render(request, 'account/base.html')


def login(request):
    if request.method == "POST":
        # Get the post parameters
        uname = request.POST['uname']
        pass1 = request.POST['pass1']
        user1 = authenticate(username=uname, password=pass1)
        if user1 is not None:
            login(user1)
            messages.success(request, "Successfully logged in.")
            return redirect('home')
        else:
            messages.error(request, "Invelid credentials. Please try again.")
            return redirect('home')
    return render(request, 'account/login.html')
    
    

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email1']
        phoneNo = request.POST['pho']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        #check for errorneous inputs
        #user should be under 10 characters
        if len(uname)>20:
            messages.error(request, "Username must be under 20 chareactor")
            return redirect('home')
        
        #user should be alphanumaric

        if not uname.isalnum():
            messages.error(request, "Username should be only contain letters and numbers")
            return redirect('home')
        
        #password should match

        if pass1 != pass2:
            messages.error(request, "Password do not match.")
            return redirect('home')

        



        #create the user
        myuser = User.objects.create_user(uname,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"your account has been successfully created")
        return redirect('home')
    else:
        # return HttpResponse('404-Not found')

        return render(request, 'account/signup.html')

def logout1(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
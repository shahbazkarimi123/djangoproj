from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
from django.shortcuts import get_object_or_404
from math import ceil

# Create your views here.
@login_required(login_url='/account/login')
def create(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            
            product.save()
            return redirect('home')
        else:
            return render(request, 'product/create.html', {'error':'All fields are required'})
    else:
        return render(request, 'product/create.html')


def detail(request):
    products = Product.objects.all()
    n = len(products)
    n_slide = n//4 + ceil((n/4)-(n//4)) #ceil will take float value as approx

    params ={'no_slides': n_slide, 'range':range(1,n_slide), 'product':products}

    return render(request, 'product/detail.html',params)
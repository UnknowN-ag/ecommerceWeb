from django.shortcuts import render
from django.http import HttpResponse
from shop.models import product
from math import ceil

# Create your views here.
def index(request):
    products = product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_products':n, 'range':range(1,nSlides), 'product':products}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse('we are at contact')

def tracker(request):
    return HttpResponse('we are at track')

def checkout(request):
    return HttpResponse('we are at checkout')

def productView(request):
    return HttpResponse('we are at product')

def search(request):
    return HttpResponse('we are at search')

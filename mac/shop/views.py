from django.http import HttpResponse
from django.shortcuts import render
from unicodedata import category

from .models import Product
from math import ceil

# Create your views here.
def index(request):
    #products = Product.objects.all()
    #print(products)
    #n = len(products)
    #nSlide = n//4 + ceil((n/4)-(n//4))
    #param = {'no_of_slides': nSlide, 'range': range(1,nSlide), 'products':products}
    #allProds = [[products, range(1, nSlide), nSlide], [products, range(1, len(products)), nSlide]]

    allProds = []
    catProds = Product.objects.values('category', 'id')
    #print(catProds)
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlide = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlide), nSlide])
    params = {'allProds': allProds}
    return  render(request, 'shop/index.html', params)


def contact(request):
    #return  render(request, 'shop/index.html')
    return HttpResponse("Contact Us")

def about(request):
    #return  render(request, 'shop/index.html')
    return render(request, 'shop/about.html')

def tracker(request):
    #return  render(request, 'shop/index.html')
    return HttpResponse("Track Here")

def prodView(request):
    #return  render(request, 'shop/index.html')
    return HttpResponse("Vew")

def checkout(request):
    #return  render(request, 'shop/index.html')
    return HttpResponse("Check out")

def search(request):
    #return  render(request, 'shop/index.html')
    return HttpResponse("Search Here")


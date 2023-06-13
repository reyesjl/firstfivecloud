from django.http import HttpResponse
from django.shortcuts import render
from .models import (
    ApparelProduct,
    ProductImage,
    MOTD,
)

# Example(s)
# return render(request, "index.html", context)
# return HttpResponse("Learn more about us and why we started First Five Rugby.")

def index(request):
    '''
    Routes user to the landing view
    '''
    context = {
        "location": "f5 landing page",
        "motd": True,
        "motd_message": "Welcome to F5Rugby.com! Explore our vintage jersey catalog, register for rugby camps, join rugby tours to Ireland, and stay informed with engaging articles. Proudly sponsored by Strong Lads, Canterbury of NZ, and World Rugby Shop."
    }
    return render(request, "index.html", context)

def catalog(request):
    '''
    Renders the catalog view
    '''
    collection = ApparelProduct.objects.all()
    context = {
        "location": "f5/catalog",
        "products": collection,
    }
    return render(request, "catalog.html", context)

def news(request):
    '''
    Renders the news view
    '''
    context = {
        "location": "f5/news"
    }
    return render(request, "news.html", context)

def camps(request):
    '''
    Renders the camps view
    '''
    context = {
        "location": "camps",
        "motd": True,
        "motd_message": "[Featured Camps] : Baltimore All Star Rugby Camp at Loyola Blakefield July 24 - 27, approx 4p - 10p daily."
    }
    return render(request, "camps.html", context)

def tours(request):
    '''
    Renders the tours view
    '''
    context = {
        "location": "f5/tours"
    }
    return render(request, "tours.html", context)

def info(request):
    '''
    Renders the info view
    '''
    context = {
        "location": "f5/info"
    }
    return render(request, "info.html", context)

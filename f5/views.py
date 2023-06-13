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
        "location": "home",
        "motd": True,
        "motd_message": "Welcome to F5Rugby.com! Explore our vintage jersey catalog, register for rugby camps, join rugby tours to Ireland, and stay informed with engaging articles. Proudly sponsored by Strong Lads, Canterbury of NZ, and World Rugby Shop."
    }
    return render(request, "index.html", context)

def catalog(request):
    '''
    Renders the catalog view
    '''
    products = ApparelProduct.objects.all()
    context = {
        "location": "catalog",
        "motd": True,
        "motd_message": "[Featured Items] : Check out the rugby camps we made for NOVA WRFC & our vintage jersey collection.",
        "products": products,
    }
    return render(request, "catalog.html", context)

def news(request):
    '''
    Renders the news view
    '''
    context = {
        "location": "news",
        "motd": True,
        "motd_message": "[Read More] : People like you are sharing their stories here; stay a while."
    }
    return render(request, "news.html", context)

def camps(request):
    '''
    Renders the camps view
    '''
    context = {
        "location": "camps",
        "motd": True,
        "motd_message": "[Active Camps] : Baltimore All Star Rugby Camp at Loyola Blakefield July 24 - 27, approx 4p - 10p daily."
    }
    return render(request, "camps.html", context)

def tours(request):
    '''
    Renders the tours view
    '''
    context = {
        "location": "tours",
        "motd": True,
        "motd_message": "[Booking Tours] : You must first apply for a quote, and then you move down the process."
    }
    return render(request, "tours.html", context)

def info(request):
    '''
    Renders the info view
    '''
    context = {
        "location": "info",
        "motd": True,
        "motd_message": "[Did you know?] : you can save 15% when you bundle you home and auto insurance."
    }
    return render(request, "info.html", context)

from django.http import HttpResponse
from django.shortcuts import render
from .models import (
    Product,
)

def handleHomeRoute(request):
    '''
    Displays firstfiverugby homepage with navigation to our services.
    '''
    context = {
        "nav": True,
        "location": "home",
        "motd": True,
        "motd_message": "Welcome to www.firstfiverugby.com! Have a look around for deals, and stay a while :)",
        "pageTitle": "First Five Rugby",
        "pageSubtitle": "A premier portal dedicated to growing and developing the game of rugby in North America.",
    }
    return render(request, "index.html", context)

def handleCatalogRoute(request):
    '''
    Displays the catalog with options to load our rugbycaps, the vintage jerseys, or team gear.
    '''
    products = Product.objects.all()
    context = {
        "location": "catalog",
        "motd": True,
        "motd_message": "any and all team orders will receive a 15% discount!",
        "pageTitle": "Unleash Your Passion",
        "pageSubtitle": "Unveiling a World of Authentic Jerseys, Honor Caps, and Exclusive Deals for Rugby Fans",
        "products":products,
    }
    return render(request, "catalog/index.html", context)

def handleCampsRoute(request):
    '''
    Displays the camps and allows visitors to register for them.
    '''
    camp = {
        "name":"baltimore rugby camp",
        "price":"350.00",
        "location":"Layola, va",
    }
    context = {
        "location": "camps",
        "motd": True,
        "motd_message": "only 10 spots remaining for rugby camp [updated 23mins ago]",
        "pageTitle": "Elevate Your Rugby",
        "pageSubtitle": "Unlock Your Rugby Potential by Training Like a Pro Rugby Player: Empowering Youth, Building Community, and Nurturing Champions.",
        "camp":camp,
    }
    return render(request, "camps/index.html", context)

def handleToursRoute(request):
    '''
    Displays the tours and allows visitors to explore and book them.
    '''
    tour = {
        "name": "Ireland Rugby Tour",
        "price": "Contact us for pricing",
        "location": "Ireland",
    }
    context = {
        "location": "tours",
        "motd": True,
        "motd_message": "Book now and receive a complimentary Irish rugby jersey! [Limited time offer]",
        "pageTitle": "The Ultimate Rugby Experience",
        "pageSubtitle": "Explore Ireland, Play Against Local Teams, and Immerse Yourself in Rugby Culture: Unforgettable Team Tours to Ireland.",
        "tour": tour,
    }
    return render(request, "tours/index.html", context)


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
        "location": "home",
        "motd": True,
        "motd_message": "Welcome to www.firstfiverugby.com! Have a look around for deals, and stay a while :)",
        "pageTitle": "First Five Rugby",
        "pageSubtitle": "A premier portal dedicated to growing and developing the game of rugby in North America.",
    }
    return render(request, "index.html", context)

def handleAboutRoute(request):
    '''
    Displays firtfiverugby about us page.
    '''
    context = {
        "location":"about",
        "motd": True,
        "motd_message": "Did you know that rugby is one of the fastest-growing sports in North America? With a staggering 40% increase in participation over the past five years, the passion for this incredible game is soaring.",
        "pageTitle":"Learn More About Us",
        "pageSubtitle":"Revolutionizing rugby in North America through innovation, collaboration, and transformative experiences for players, driving game growth."
    }
    return render(request, "about.html", context)

def handleCatalogRoute(request):
    '''
    Displays the catalog with options to load our rugbycaps, the vintage jerseys, or team gear.
    '''
    products = Product.objects.all()
    context = {
        "location": "catalog",
        "motd": True,
        "motd_message": "any and all team orders will receive a 15% discount!",
        "pageTitle": "Our Catalog",
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
        "motd_message": "only 7 spots remaining for rugby camp [updated 23mins ago]",
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
        "motd_message": "our tours typically run 1/2 the price of others with amazing games, training, lodging, and culture",
        "pageTitle": "The Ultimate Rugby Experience",
        "pageSubtitle": "Explore Ireland, Play Against Local Teams, and Immerse Yourself in Rugby Culture: Unforgettable Team Tours to Ireland.",
        "tour": tour,
    }
    return render(request, "tours/index.html", context)

from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.shortcuts import render
from .models import (
    Product, Inquiry
)

def handleHomeRoute(request):
    '''
    Displays firstfiverugby homepage with navigation to our services.
    '''
    context = {
        "location": "home",
        "motd": True,
        "motd_message": "Welcome to www.firstfiverugby.com! Enjoy your favorite place to spend time off the pitch or at work! [24/7 access]",
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
        "motd_message": "5% discount on all team order [updated 5mins ago]",
        "products":products,
    }
    return render(request, "catalog/index.html", context)

@csrf_protect
def handleCampsRoute(request):
    '''
    Displays the camps and allows visitors to file an inquiry.
    '''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        service = request.POST.get('service')

        # Create a new Inquiry object
        inquiry = Inquiry(name=name, email=email, number=number, service=service)
        inquiry.save()

        # Redirect to the success page after saving the inquiry
        return render(request, "camps/success.html", context)
    
    context = {
        "location": "camps",
        "motd": True,
        "motd_message": "only 7 spots remaining for rugby camp [updated 23mins ago]",
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
        "tour": tour,
    }
    return render(request, "tours/index.html", context)

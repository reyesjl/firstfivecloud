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
        "activelink": "home",
    }
    return render(request, "index.html", context)

def handleAboutRoute(request):
    '''
    Displays firtfiverugby about us page.
    '''
    context = {
        "activelink":"home",
    }
    return render(request, "index-copy.html", context)

def handleCatalogRoute(request):
    '''
    Displays the catalog with options to load our rugbycaps, the vintage jerseys, or team gear.
    '''
    products = Product.objects.all()
    context = {
        "activelink":"catalog",
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
        "activelink":"camps",
        'registered': True,
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
        "activelink":"tours",
        "tour": tour,
    }
    return render(request, "tours/index.html", context)

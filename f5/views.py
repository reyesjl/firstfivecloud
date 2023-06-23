from django.http import HttpResponse
from django.shortcuts import render
from .models import (
    Product,
    Article
)

# Example(s)
# return render(request, "index.html", context)
# return HttpResponse("Learn more about us and why we started First Five Rugby.")

def index(request):
    '''
    Routes user to the landing view
    '''
    context = {
        "nav": True,
        "location": "home",
        "motd": True,
        "motd_message": "Welcome to www.firstfiverugby.com! Look out for deal of the week $",
        "pageTitle": "First Five Rugby",
        "pageSubtitle": "A premier portal dedicated to growing and developing the game of rugby in North America.",
    }
    return render(request, "index.html", context)

def catalog(request):
    '''
    Renders the catalog view
    '''
    products = Product.objects.all()
    context = {
        "location": "catalog",
        "motd": True,
        "motd_message": "such emtpy here -.-",
        "pageTitle": "Catalog",
        "pageSubtitle": "Browse our wide range of rugby apparel products.",
        "products": products,
    }
    return render(request, "catalog.html", context)

def news(request):
    '''
    Renders the news view
    '''
    articles = Article.objects.all()
    context = {
        "location": "news",
        "motd": True,
        "motd_message": "such empty here -.-",
        "pageTitle": "News",
        "pageSubtitle": "Stay updated with the latest rugby news and stories.",
        "articles":articles,
    }
    return render(request, "news.html", context)

def article(request, id):
    '''
    Renders an article view
    '''
    article = Article.objects.get(id=id)
    context = {
        "nav": False,
        "location": "news",
        "motd": True,
        "motd_message": article.tags,
        "pageTitle": article.title,
        "pageSubtitle": article.small_description,
        "article":article,
    }
    return render(request, "article.html", context)

def camps(request):
    '''
    Renders the camps view
    '''
    context = {
        "location": "camps",
        "motd": True,
        "motd_message": "such empty here -.-",
        "pageTitle": "Camps",
        "pageSubtitle": "Join our rugby camps and enhance your skills.",
    }
    return render(request, "camps.html", context)

def tours(request):
    '''
    Renders the tours view
    '''
    context = {
        "location": "tours",
        "motd": True,
        "motd_message": "such emtpy here -.-",
        "pageTitle": "Tours",
        "pageSubtitle": "Explore our exciting rugby tour packages.",
    }
    return render(request, "tours.html", context)

def info(request):
    '''
    Renders the info view
    '''
    context = {
        "location": "info",
        "motd": True,
        "motd_message": "this section is still being built!",
        "pageTitle": "Info",
        "pageSubtitle": "Get useful information about rugby and related services.",
    }
    return render(request, "info.html", context)

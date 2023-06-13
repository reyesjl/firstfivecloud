from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, RugbyCamp

# Example(s)
# return render(request, "index.html", context)
# return HttpResponse("Learn more about us and why we started First Five Rugby.")

def index(request):
    '''
    Routes user to the landing view
    '''
    return render(request, "index.html")

def catalog(request):
    return render(request, "catalog.html")

def news(request):
    latest_posts = Article.objects.order_by("title")
    return render(request, "news.html")

def camps(request):

    # fetch camps...
    latest_camps = RugbyCamp.objects.order_by("-startdate")
    return render(request, "camps.html")

def tours(request):
    
    # fetch tours...

    return render(request, "tours.html")

def info(request):
    return render(request, "info.html")

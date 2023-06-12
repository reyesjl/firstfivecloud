from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, RugbyCamp

def index(request):
    '''
    Routes user to the landing view
    '''
    context = {
       "message_otd": "welcome to f5 rugby. checkout our catalogs, register for camps, find a quote for your tours, and much more!" 
    }
    return render(request, "index.html", context)

def about(request):
    return HttpResponse("Learn more about us and why we started First Five Rugby.")

def catalog(request):
    return HttpResponse("Browse our extensive collection, find something for you.")

def news(request):
    latest_posts = Article.objects.order_by("")
    return 

def camps(request):
    latest_camps = RugbyCamp.objects.order_by("-startdate")
    return HttpResponse("Grow your rugby skills and make valuable connections.")

def tours(request):
    return HttpResponse("Tours to Ireland are here and you can get a quote too.") 

def help(request):
    return HttpResponse("Have a question for our team?")

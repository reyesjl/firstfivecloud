from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the F5 platform")

def about(request):
    return HttpResponse("Learn more about us and why we started First Five Rugby.")

def catalog(request):
    return HttpResponse("Browse our extensive collection, find something for you.")

def news(request):
    return HttpResponse("Keep up with the latest rugby news here.")

def camps(request):
    return HttpResponse("Grow your rugby skills and make valuable connections.")

def tours(request):
    return HttpResponse("Tours to Ireland are here and you can get a quote too.") 

def help(request):
    return HttpResponse("Have a question for our team?")

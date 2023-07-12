from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def handleLoginUser(request):
    '''
    This view handles the login form.
    '''
    return render(request, 'authenticate/login.html', {})
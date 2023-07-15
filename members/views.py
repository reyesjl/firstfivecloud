from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def handleLoginUser(request):
    """
    This view handles the login form.
    """
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home", {"user": user})
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect("login")
    return render(request, "authenticate/login.html", {})


def handleSignupUser(request):
    """
    This view handles the signup form.
    """
    return render(request, "authenticate/signup.html", {})

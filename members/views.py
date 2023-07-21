from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def handleSignup(request):
    """
    Handles the signup of a new user
    """
    if request.method == "POST":
        # Get the POST data
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        # Create the user
        user = User.objects.create_user(
            username=username, password=password, email=email
        )
        user.save()

        # Log the user in
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully signed up!")
            return redirect("home")
    return render(request, "authenticate/signup.html")


def handleLogin(request):
    """
    Handles the login of an existing user
    """
    if request.method == "POST":
        # Get the POST data
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # If user is authenticated, log them in and redirect to home
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials, please try again.")
            return redirect("login")
    return render(request, "authenticate/login.html")


def handleLogout(request):
    """
    Handles the logout of a user
    """
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect("home")

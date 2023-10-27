from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render

User = get_user_model()

def handleSignupUser(request):
    """
    Sign up user to platform.
    """
    # Your code for signup
    return render('signup.html')

def handleLoginUser(request):
    """
    Log a user into the system.
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User is authenticated.')
            return redirect('home')
        else:
            messages.error(request, 'User is NOT authenticated.')  # Use error instead of success for error messages
            return redirect('login')
    else:
        # Your code for login
        return render('login.html')

def handleLogoutUser(request):
    """
    Log a user out of the system.
    """
    logout(request)
    messages.success(request, 'User has been logged out.')
    return redirect('logout.html')
from django.contrib.auth import get_user_model, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import FFRSignupForm, FFRLoginForm
from django.contrib.auth.decorators import login_required
from f5.models import EventTicket


User = get_user_model()

def handleSignupUser(request):
    if request.method == "POST":
        form = FFRSignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # This will create and save the user to the database
            login(request, user)  # Log in the user after registration
            messages.success(request, 'User has been registered and logged in.')
            return redirect('dashboard', username=user.username)  # Redirect to the home page after successful registration
    else:
        form = FFRSignupForm()

    context = {"form": form}
    
    return render(request, 'signup.html', context)


@login_required
def handleDashboardRoute(request, username):
    # Query all EventTickets
    event_tickets = EventTicket.objects.all()  # You can add filters here if needed

    context = {
        "user": request.user,
        "event_tickets": event_tickets,
    }

    return render(request, 'dashboard.html', context)

def handleLoginUser(request):
    if request.method == "POST":
        form = FFRLoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'User is authenticated.')
            return redirect('dashboard', username=user.username)  # Redirect to the home page after successful login
        else:
            messages.error(request, 'User is NOT authenticated.')
    else:
        form = FFRLoginForm()

    context = {"form": form}
    
    return render(request, 'login.html', context)


def handleLogoutUser(request):
    """
    Log a user out of the system.
    """
    logout(request)
    messages.success(request, 'User has been logged out.')

    return redirect('login')
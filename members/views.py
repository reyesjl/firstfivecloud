from django.contrib.auth import get_user_model, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import FFRSignupForm, FFRLoginForm
from django.contrib.auth.decorators import login_required
from f5.models import Event, EventTicket
from .decorators import coach_required


User = get_user_model()

def handleSignupUser(request):
    if request.method == "POST":
        form = FFRSignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # This will create and save the user to the database
            login(request, user)  # Log in the user after registration
            messages.success(request, 'User has been registered and logged in.')
            return redirect('dashboard')  # Redirect to the home page after successful registration
    else:
        form = FFRSignupForm()

    context = {"form": form}
    
    return render(request, 'signup.html', context)


@login_required
def handleDashboardRoute(request):
    is_coach = request.user.groups.filter(name='coach').exists()
    is_admin = request.user.groups.filter(name='admin').exists()
    is_player = request.user.groups.filter(name='player').exists()

    events = Event.objects.all()  # Get all events

    selected_event = None
    event_tickets = []

    if request.method == 'POST':
        event_id = request.POST.get('event')
        if event_id:
            selected_event = get_object_or_404(Event, pk=event_id)
            event_tickets = EventTicket.objects.filter(camp=selected_event)

    context = {
        "user": request.user,
        "events": events,
        "event_tickets": event_tickets,
        "selected_event": selected_event,
    }
    
    if (is_coach):
        return render(request, 'coach_dashboard.html', context)
    elif (is_player):
        return render(request, 'player_dashboard.html', context)
    elif(is_admin):
        return render(request, 'admin_dashboard.html', context)
    else:
        return render(request, 'dashboard.html', context)
    

@login_required
def handleCoachDashboardRoute(request):
    events = Event.objects.all()  # Get all events

    selected_event = None
    event_tickets = []

    if request.method == 'POST':
        event_id = request.POST.get('event')
        if event_id:
            selected_event = get_object_or_404(Event, pk=event_id)
            event_tickets = EventTicket.objects.filter(camp=selected_event)

    context = {
        "user": request.user,
        "events": events,
        "event_tickets": event_tickets,
        "selected_event": selected_event,
    }

    return render(request, 'dashboard.html', context)

def handleLoginUser(request):
    if request.method == "POST":
        form = FFRLoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'User is authenticated.')
            return redirect('dashboard')  # Redirect to the home page after successful login
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
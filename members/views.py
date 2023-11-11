from django.contrib.auth import get_user_model, login, logout
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from teams.models import Team
from .forms import FFRSignupForm, FFRLoginForm, AlterUserForm
from django.contrib.auth.decorators import login_required
from f5.models import Event, EventTicket
from .decorators import coach_required


User = get_user_model()

def handleSignupUser(request):
    if request.method == "POST":
        form = FFRSignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # This will create and save the user to the database
            # login(request, user)  # Log in the user after registration
            messages.success(request, 'User has been registered')
            
            # Send a confirmation email
            subject = 'Account Created'
            message = f"""Welcome {user.username},

        Your account was created successfully, please visit www.firstfiverugby.com/members/login 

        Have a great day, and thank you for being a member!
        
        First Five Rugby
        www.firstfiverugby.com
        letusknow@firstfiverugby.com
            """
            from_email = 'firstfiverugby@gmail.com'  # Replace with your email
            recipient_list = [user.email]
            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
            )

            return redirect('login')  # Redirect to the home page after successful registration
    else:
        form = FFRSignupForm()

    context = {"form": form}
    
    return render(request, 'signup.html', context)

def handleMembersRoute(request):
    users = User.objects.all() 
    context = {
        'users': users,
        'member_count': users.count(),
    }
    return render(request, "members.html", context)

def handleProfileRoute(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        "profile": user,
    }

    return render(request, 'profile.html', context)

@login_required
def handleEditProfileRoute(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.user != user:
        # Redirect the user or display an error message
        messages.error(request, "You are not allowed to edit this user's profile.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = AlterUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the profile page or another appropriate URL

    else:
        form = AlterUserForm(instance=user)

    context = {
        'profile': user,
        'form': form,
    }

    return render(request, 'edit_profile.html', context)

@login_required
def handleDashboardRoute(request):    
    user = request.user
    context = {
        "user": user,
    }
    
    is_coach = user.groups.filter(name='coach').exists()
    is_admin = user.groups.filter(name='admin').exists()
    is_player = user.groups.filter(name='player').exists()

    if is_coach:
        coached_teams = Team.objects.filter(coach=user)
        coached_events = Event.objects.filter(coach=user)
        
        events = Event.objects.all().order_by('-date')
        selected_event = None
        event_tickets = []
        if request.method == 'POST':
            event_id = request.POST.get('event')
            if event_id:
                selected_event = get_object_or_404(Event, pk=event_id)
                event_tickets = EventTicket.objects.filter(camp=selected_event)
        
        context.update({
            "coached_teams": coached_teams,
            "coached_events": coached_events,
            "selected_event": selected_event,
            "event_tickets": event_tickets,
        })
        
        return render(request, 'dashboards/coach_dashboard.html', context)
    
    if is_player:
        # Handle player-specific logic here
        # Fetch player-related data and render 'player_dashboard.html'
        return render(request, 'dashboards/player_dashboard.html', context)
    
    if is_admin:
        events = Event.objects.all().order_by('-date')
        selected_event = None
        event_tickets = []
        if request.method == 'POST':
            event_id = request.POST.get('event')
            if event_id:
                selected_event = get_object_or_404(Event, pk=event_id)
                event_tickets = EventTicket.objects.filter(camp=selected_event)
        
        context.update({
            "events": events,
            "event_tickets": event_tickets,
            "selected_event": selected_event,
        })
        # Handle admin-specific logic here
        # Fetch admin-related data and render 'admin_dashboard.html'
        return render(request, 'dashboards/admin_dashboard.html', context)

    # Default dashboard for users with no specific role
    return render(request, 'dashboards/dashboard.html', context)
    
def handleLoginUser(request):
    if request.method == "POST":
        form = FFRLoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'User is authenticated.')
            return redirect('home')  # Redirect to the home page after successful login
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
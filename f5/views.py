from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.utils import timezone
from .models import Event, EventTicket
from .forms import EventTicketForm
import random
from dotenv import load_dotenv
import stripe

# Load env file terminology
load_dotenv()

def handleHomeRoute(request):
    """
    Displays home route.
    """
     # Filter events with dates that have not yet passed
    current_date = timezone.now()
    camp_events = Event.objects.filter(date__gte=current_date).order_by('date') 

    # Select the first 10 upcoming events
    events = camp_events[:10]

    context = {
        "activelink": 0,
        "events": events,
    }
    return render(request, "home.html", context)

def handleAboutRoute(request):
    """
    Display about page.
    """
    context = {
        "activelink": 6,
    }
    return render(request, "about.html", context)

def handleResearchRoute(request):
    """
    Display research page.
    """

    context = {
        "activelink": 7,
    }
    return render(request, "research.html", context)

def handlePartnersRoute(request):
    """
    Render the partners page.
    """
    context = {
        "activelink": 0,
    }
    return render(request, "partners.html", context)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# MOVE TO PLAYERS APP WHEN READY 
def handlePlayersRoute(request):
    """
    Show the players page.
    """
    
    current_date = timezone.now()
    camp_events = Event.objects.filter(date__gte=current_date).order_by('date') 
    events = camp_events[:5]

    context = {
        "activelink": 1,
        "events": events,
    }
    return render(request, "players.html", context)

# MOVE TO COACHES APP ?????
def handleCoachesRoute(request):
    """
    Show coaches page.
    """
    context = {
        "activelink": 4
    }
    return render(request, "coaches.html", context)

# MOVE TO TEAMS APP
def handleSchedulesRoute(request):
    """
    Show the schedules page.
    """
    context = {
        "activelink": 5,
    }
    return render(request, "schedules.html", context)


# MOVE TO STORE APP
def handleStoreRoute(request):
    """
    Show the store page.
    """

    stripe.api_key = "sk_test_51Ny5LQI2LlT0b19fVnX2tj76wVyxmcJLxBIZgOcTZD5BKoDy5PPHuZkjjdeknHp5wQjo2tA8Paj3GgjDFNypyTJh00gI5FLlPb"
    
    # Retrieve a list of all products
    products = stripe.Product.list(limit=100)

    context = {
        "activelink": 3,
        "products": products,
    }

    return render(request, "store.html", context)

# MOVE WHERE HMMM ?
def handleCampsRoute(request):
    """
    Display upcoming camp information.
    """
    current_date = timezone.now()
    camp_events = Event.objects.filter(category="festival", date__gte=current_date).order_by('date')
    pathway_events = Event.objects.filter(category="pathways", date__gte=current_date).order_by('date')
    context = {
        "activelink": 1,
        "camp_events": camp_events,
        "pathway_events": pathway_events,
    }
    return render(request, "camps.html", context)

def handleCampDetailsRoute(request, id):
    """
    Display the details for a specific camp
    """
    camp = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        # django forms does the magic here for me
        form = EventTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False) # save for now, but I need to add the camp in there
            ticket.camp = camp  # Link the ticket to the specific camp
            ticket.save()
            # Send a confirmation email
            subject = 'Rugby Event'
            message = f"""Hello {ticket.parent_full_name},

            Your child, {ticket.player_full_name} has been registered for the following camp:
            
            Camp Details
            Title: {ticket.camp.title}
            Date: {ticket.camp.date}
            Time: {ticket.camp.time}
            Location: {ticket.camp.location}
            Hosted By: {ticket.camp.hosted_by}
            
            First Five Rugby
            www.firstfiverugby.com
            letusknow@firstfiverugby.com
            """
            from_email = 'firstfiverugby@gmail.com'  # Replace with your email
            recipient_list = [ticket.parent_email]
            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
            )
            return redirect('campsuccess', id=id)
    else:
        form = EventTicketForm()

    context = {
        'event': camp, 
        'form': form,
    }
    return render(request, "campdetails.html", context)

# MOVE TO EVENTS ?
def handleToursRoute(request):
    """
    Render the tours page.
    """
    context = {
        "activelink": 5
    }
    return render(request, "tours.html", context)

def handleCampSuccessRoute(request, id):
    """
    Show success message to the user for camp registration.
    """
    camp = get_object_or_404(Event, id=id)
    attendees = EventTicket.objects.filter(camp=camp).count
    context = {
        "activelink": 0,
        "event": camp,
        "attendees": attendees,
    }
    return render(request, "campsuccess.html", context)
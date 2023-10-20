from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Team, Fixture, Product, Event, EventTicket
from .forms import EventTicketForm
import os, requests, random
from dotenv import load_dotenv
import stripe

# Load env file terminology
load_dotenv()

def handleHomeRoute(request):
    """
    Displays home route.
    """
    featured_products = Product.objects.filter(category__name='featured', is_active=True)

    camp_events = Event.objects.all().order_by('date') 
    events = camp_events[:10]

    context = {
        "activelink": 0,
        "featured_products": featured_products,
        "events": events,
    }
    return render(request, "home.html", context)

def handleResearchRoute(request):
    """
    Display research page.
    """

    context = {
        "activelink": 0,
    }
    return render(request, "research.html", context)

def handleAboutRoute(request):
    """
    Display about page.
    """
    context = {
        "activelink": 6,
    }
    return render(request, "about.html", context)

def handlePlayersRoute(request):
    """
    Show the players page.
    """
    camp_events = Event.objects.all().order_by('date') 
    events = camp_events[:5]
    player_deal_products = Product.objects.filter(category__name='player_deal', is_active=True)
    context = {
        "activelink": 1,
        "player_deal_products": player_deal_products,
        "events": events,
    }
    return render(request, "players.html", context)

def handleCoachesRoute(request):
    """
    Show coaches page.
    """
    context = {
        "activelink": 4
    }
    return render(request, "coaches.html", context)

def handleTeamsRoute(request):
    """
    Show a temporary static teams page.
    """
    teams = Team.objects.all()
    context = {
        "activelink": 2,
        "teams":teams,
    }
    return render(request, "teams.html", context)

def handleFetchTeamDetailsRoute(request, id):
    """
    Fetch the details of a specific team by ID.
    """
    team = get_object_or_404(Team, id=id)
    context = {
        "activelink": 2,
        "team":team,
    }
    return render(request, 'teamdetails.html', context)

def handleFetchTeamFixturesRoute(request, id):
    """
    Fetch team fixtures by ID.
    """
    team = get_object_or_404(Team, id=id)
    fixtures = Fixture.objects.filter(Q(team_1=team) | Q(team_2=team)).order_by('date_played')

    context = {
        "activelink": 2,
        "team": team,
        "fixtures": fixtures,
    }
    return render(request, 'teamfixtures.html', context)

def handleSchedulesRoute(request):
    """
    Show the schedules page.
    """
    context = {
        "activelink": 5,
    }
    return render(request, "schedules.html", context)

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

def handleFetchProductDetailsRoute(request, id):
    """
    Display a product on its own.
    """
    product = get_object_or_404(Product, id=id)
    context = {
        "activelink": 3,
        "product": product
    }

    return render(request, "productdetails.html", context)

def handleCampsRoute(request):
    """
    Display upcoming camp information.
    """
    camp_events = Event.objects.filter(category="festival").order_by('date')
    pathway_events = Event.objects.filter(category="pathways").order_by('date')
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
    random_teams = ''
    if request.method == 'POST':
        # django forms does the magic here for me
        form = EventTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False) # save for now, but I need to add the camp in there
            ticket.camp = camp  # Link the ticket to the specific camp
            ticket.save()
            return redirect('campsuccess', id=id)
    else:
        form = EventTicketForm()

        total_teams = Team.objects.count()
        # Check if there are at least 3 teams in the table
        if total_teams >= 3:
            # Generate 3 random unique indices within the range of total_teams
            random_indices = random.sample(range(total_teams), 3)

            # Fetch the teams using the random indices
            random_teams = Team.objects.all()[random_indices[0]:random_indices[0] + 3]

    context = {
        'event': camp, 
        'form': form,
        'random_teams': random_teams,
    }
    return render(request, "campdetails.html", context)

def handleToursRoute(request):
    """
    Render the tours page.
    """
    context = {
        "activelink": 5
    }
    return render(request, "tours.html", context)

def handlePartnersRoute(request):
    """
    Render the partners page.
    """
    context = {
        "activelink": 0,
    }
    return render(request, "partners.html", context)

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
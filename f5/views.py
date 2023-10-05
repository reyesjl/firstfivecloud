from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Team, Fixture, Product, Event
from django.http import JsonResponse
import os, requests
from dotenv import load_dotenv

# Load env file terminology
load_dotenv()

def handleHomeRoute(request):
    """
    Displays firstfiverugby homepage with navigation to our services.
    """
    context = {
        "activelink": "home",
    }
    return render(request, "home.html", context)

def handleAboutRoute(request):
    """
    Displays firtfiverugby about us page.
    """
    context = {
        "activelink": 1,
    }
    return render(request, "about.html", context)

def handleSuccessRoute(request):
    """
    Show success message for the user.
    """
    context = {
        "activelink": "success",
    }
    return render(request, "success.html", context)

"""
**** SINCE PREVIEW UPDATES 9/12/2023 ****
"""

def handlePreviewRoute(request):
    """
    Displays a preview route for devs to see new content. 
    """
    featured_products = Product.objects.filter(category__name='featured', is_active=True)
    
    upcoming_events = Event.objects.all()
    next_three_events = upcoming_events[:3]

    context = {
        "activelink": 0,
        "featured_products": featured_products,
        "events": next_three_events,
    }
    return render(request, "preview.html", context)

def handlePlayersRoute(request):
    """
    Show the players page.
    """
    player_deal_products = Product.objects.filter(category__name='player_deal', is_active=True)
    context = {
        "activelink": 1,
        "player_deal_products": player_deal_products,
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
    featured_products = Product.objects.filter(category__name="featured", is_active=True)
    team_products = Product.objects.filter(category__name="team", is_active=True)
    rare_products = Product.objects.filter(category__name="rare", is_active=True)
    common_products = Product.objects.filter(category__name="common", is_active=True)
    archived_products = Product.objects.filter(category__name="jersey", is_active=False)

    context = {
        "activelink": 3,
        "featured_products": featured_products,
        "team_products": team_products,
        "rare_products": rare_products,
        "common_products": common_products,
        "archived_products": archived_products,
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
    context = {
        "activelink": 1,
    }
    return render(request, "camps.html", context)

def handleCampDetailsRoute(request):
    """
    Return camp details page.
    """
    context = {
        "activelink": 1,
    }

    return render(request, "campdetails.html", context)

def handleToursRoute(request):
    """
    Render the tours page.
    """
    context = {
        "activelink": 2
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
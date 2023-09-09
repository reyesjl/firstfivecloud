from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Team, Fixture

def handleHomeRoute(request):
    """
    Displays firstfiverugby homepage with navigation to our services.
    """
    context = {
        "activelink": "home",
    }
    return render(request, "home.html", context)

def handlePreviewRoute(request):
    """
    Displays a preview route for devs to see new content. 
    """
    context = {
        "activelink": 0,
    }
    return render(request, "preview.html", context)

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
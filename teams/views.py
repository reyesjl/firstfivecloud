from django.db.models import Q
from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404, render

from f5 import models
import teams
from .models import Team, Match, MatchEvent, League, Roster, Player
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def handleTeamsRoute(request):
    """
    Return the teams page.
    """
    recent_matches = Match.objects.order_by('-date')[:6]
    leagues = League.objects.all()

    # Group the matches by date
    grouped_matches = {}
    for match in recent_matches:
        date = match.date
        if date not in grouped_matches:
            grouped_matches[date] = []
        grouped_matches[date].append(match)
    
    context = {
        "activelink": 2,
        "grouped_matches": grouped_matches,
        "leagues": leagues,
    }
    return render(request, "teams.html", context)

def handleTeamRoute(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    try:
        roster = Roster.objects.get(team=team)
        starting_23 = roster.starting_23.all()
        reserves = roster.reserves.all()
    except Roster.DoesNotExist:
        # Handle the case where the roster doesn't exist for the team
        starting_23 = []
        reserves = []

    recent_matches = Match.objects.filter(
        (Q(team1=team) & Q(team1__league=team.league)) | (Q(team2=team) & Q(team2__league=team.league))
    ).order_by('-date')


    # Group the matches by date
    grouped_matches = {}
    for match in recent_matches:
        date = match.date
        if date not in grouped_matches:
            grouped_matches[date] = []
        grouped_matches[date].append(match)

    # You can customize the context to include more information as needed
    context = {
        'team': team,
        'roster': starting_23,
        'reserves': reserves,
        'grouped_matches': grouped_matches,
        'activelink': 9,  
    }

    # Render a template to display the team's details and roster
    return render(request, 'team.html', context)

def handleMatchesRoute(request):
    # Retrieve recent matches and order them by date
    recent_matches = Match.objects.order_by('-date')

    # Group the matches by date
    grouped_matches = {}
    for match in recent_matches:
        date = match.date
        if date not in grouped_matches:
            grouped_matches[date] = []
        grouped_matches[date].append(match)

    # Create a list of matches by flattening the grouped_matches dictionary
    matches_list = [match for matches in grouped_matches.values() for match in matches]

    # Number of matches to display per page
    matches_per_page = 10

    # Get the current page from the request's GET parameters
    page = request.GET.get('page')

    # Create a paginator for the list of matches
    paginator = Paginator(matches_list, matches_per_page)

    try:
        # Get the selected page of matches
        paginated_matches = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver the first page
        paginated_matches = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page
        paginated_matches = paginator.page(paginator.num_pages)

    context = {
        "activelink": 2,
        "paginated_matches": paginated_matches,
        "grouped_matches": grouped_matches,
    }
    return render(request, "matches.html", context)

def handleMatchDetailsRoute(request, match_id):
    """
    Return details for a match.
    """
    match = get_object_or_404(Match, id=match_id)

    context = {
        'activelink': 3,
        'match': match,
    }

    return render(request, 'matchdetails.html', context)

def handleLeagueRoute(request, league_id):
    if league_id is not None:
        league = League.objects.filter(id=league_id).first()
        # Replace the following line with code to get the teams associated with the league
        league_teams = league.teams.all()  # Replace with the appropriate way to get the teams
    else:
        league = None
        league_teams = None
    
    context = {
        "activelink": 3,
        "league": league,
        "teams": league_teams,
    }
    return render(request, 'league.html', context)


def handlePlayerDetailsRoute(request, player_id):
    if player_id is not None:
        player = Player.objects.filter(id=player_id).first()  # Filter players by the given player ID
    else:
        player = None

    context = {
        'activelink': 3,
        'player': player,
    }

    return render(request, 'playerdetails.html', context)
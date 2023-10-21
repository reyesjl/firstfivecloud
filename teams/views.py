from django.shortcuts import render
from .models import Team, Match, MatchEvent
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def handleTeamsRoute(request):
    """
    Return the teams page.
    """
     # Retrieve the 6 most recent matches from the 'Division 1 College' league
    recent_matches = Match.objects.filter(team1__league='Division 1 College', team2__league='Division 1 College').order_by('-date')[:6]

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
    }
    return render(request, "teams.html", context)

def handleMatchesRoute(request):
    # Retrieve recent matches and order them by date
    recent_matches = Match.objects.filter(team1__league='Division 1 College', team2__league='Division 1 College').order_by('-date')

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

from django.shortcuts import get_object_or_404, render
from .models import Team, Match, MatchEvent, League, Roster
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def handleTeamsRoute(request):
    """
    Return the teams page.
    """
     # Retrieve the 6 most recent matches from the 'Division 1 College' league
    recent_matches = Match.objects.order_by('-date')[:6]

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

def handleTeamDetailsRoute(request, team_name):
    # Retrieve the team with the specified name or handle a 404 error if it doesn't exist
    team = get_object_or_404(Team, name=team_name)

    # Retrieve the roster for the team using the Roster model
    try:
        roster = Roster.objects.get(team=team)
        starting_23 = roster.starting_23.all()
        reserves = roster.reserves.all()
    except Roster.DoesNotExist:
        # Handle the case where the roster doesn't exist for the team
        starting_23 = []
        reserves = []

    # You can customize the context to include more information as needed
    context = {
        'team': team,
        'roster': starting_23,
        'reserves': reserves,
        'activelink': 9,  # Assuming this is the active link for team details
    }

    # Render a template to display the team's details and roster
    return render(request, 'teamdetails.html', context)

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

def handleAllAmericanProLeagueRoute(request):
    """
    Return the league's homepage
    """
    league_title = "All American Pro"  # Replace with the actual title of your league

    # First, retrieve the league with the specified title
    leagues = League.objects.filter(title=league_title)

    # Check if the league exists
    if leagues.exists():
        # If there are multiple leagues with the same title, you can choose one based on your criteria.
        # For example, you can choose the first one:
        league = leagues.first()
        
        # Now, retrieve all the teams associated with the league
        teams = Team.objects.filter(league=league)
        
        # Create a list of dictionaries containing team name and crest
        team_data = [{'name': team.name, 'crest': team.crest} for team in teams]
    else:
        # Handle the case where the league doesn't exist
        team_data = []  # Initialize an empty list

    context = {
        "activelink": 8,
        "standings": team_data,
    }
    return render(request, "all-american-pro.html", context)
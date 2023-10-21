import random
import datetime
from teams.models import Match, Team 

# Fetch teams from the 'Division 1 College' league
teams_division_1 = Team.objects.filter(league='Division 1 College')

# Fetch teams from the 'All-American Rugby Cup' league
teams_all_american = Team.objects.filter(league='All-American Rugby Cup')

# Create matches for 'Division 1 College' teams
matches = []
current_date = datetime.date(2023, 1, 7)  # Start from the first Saturday of the year
for i in range(len(teams_division_1)):
    team1 = teams_division_1[i]
    team2 = random.choice(teams_division_1.exclude(id=team1.id))  # Ensure team2 is different from team1

    # Simulate scores
    team1_score = random.randint(0, 50)
    team2_score = random.randint(0, 50)

    match = Match(
        date=current_date,
        time='12:00:00',  # Set the time as needed
        location='Neutral',  # Set the location as needed
        team1=team1,
        team2=team2,
        team1_score=team1_score,
        team2_score=team2_score,
    )
    matches.append(match)

    # Move to the next Saturday
    current_date += datetime.timedelta(days=7)

# Create matches for 'All-American Rugby Cup' teams
for i in range(len(teams_all_american)):
    team1 = teams_all_american[i]
    team2 = random.choice(teams_all_american.exclude(id=team1.id))  # Ensure team2 is different from team1

    # Simulate scores
    team1_score = random.randint(0, 50)
    team2_score = random.randint(0, 50)

    match = Match(
        date=current_date,
        time='12:00:00',  # Set the time as needed
        location='Neutral',  # Set the location as needed
        team1=team1,
        team2=team2,
        team1_score=team1_score,
        team2_score=team2_score,
    )
    matches.append(match)

# Bulk insert the matches into the database
Match.objects.bulk_create(matches)
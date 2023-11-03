import random
from datetime import date, time, timedelta
from django.utils import timezone
from teams.models import Match, Team, League

Match.objects.all().delete()

# Define the number of weeks and matches per week
num_weeks = 18
matches_per_week = 5  # Adjust as needed

# Define the start date for the matches
start_date = date(2023, 1, 1)

# Get a list of all leagues
leagues = League.objects.all()

# Loop through each league
for league in leagues:
    teams_in_league = list(league.teams.all())  # Convert the queryset to a list

    for week in range(num_weeks):
        for _ in range(matches_per_week):
            # Randomly select two teams from the same league for a match
            team1, team2 = random.sample(teams_in_league, 2)

            # Simulate game outcomes (you can replace this with your own logic)
            team1_score = random.randint(0, 50)
            team2_score = random.randint(0, 50)

            match_date = start_date + timedelta(weeks=week, days=random.randint(0, 6))
            match_time = time(random.randint(10, 18), random.randint(0, 59))
            location = f"Stadium {random.randint(1, 5)}"

            match = Match(
                date=match_date,
                time=match_time,
                location=location,
                team1=team1,
                team2=team2,
                team1_score=team1_score,
                team2_score=team2_score,
            )
            match.save()
            print(f"Created match: {match}")

print("Match creation and simulation completed.")

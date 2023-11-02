import random
from datetime import date, timedelta

from teams.models import Team, Match, MatchEvent

# Define the start and end dates of the pro Rugby season
start_date = date(2022, 2, 24)  # Adjust the year as needed
end_date = date(2022, 7, 8)     # Adjust the year as needed

# Retrieve the teams
teams = Team.objects.all()

# Shuffle the teams to randomize the order
teams = list(teams)
random.shuffle(teams)

# define number of rounds
num_rounds = 18

# Calculate the total number of matches each team should play
matches_per_team = num_rounds - 2  # 2 bye weeks for each team

# Initialize the match week counter
match_week = 1

# Create matches and events for the season
current_date = start_date

for round_number in range(1, num_rounds + 1):
    # Ensure that each team plays one match per week
    for _ in range(len(teams) // 2):
        team1, team2 = teams.pop(0), teams.pop(0)
        match = Match.objects.create(
            date=current_date,
            time="15:00:00",  # Set the time as needed
            location="Stadium",  # Set the location as needed
            team1=team1,
            team2=team2,
        )

        # Initialize scores for the match
        team1_score = 0
        team2_score = 0

        # Create random match events (example)
        for _ in range(10):
            event_type = random.choice(['try', 'yellow_card', 'red_card', 'try_conversion', 'penalty_conversion', 'penalty_try'])
            minute = random.randint(1, 80)
            player = random.choice([team1, team2]).name

            # Update scores based on event type
            if event_type == 'try':
                points = 5
            elif event_type == 'try_conversion':
               points = 2
            elif event_type == 'penalty_conversion':
                points = 3
            elif event_type == 'penalty_try':
                points = 7
            else:
                points = 0

            if player == team1.name:
                team1_score += points
            else:
                team2_score += points

            # Create the match event
            MatchEvent.objects.create(
                event_type=event_type,
                minute=minute,
                player=player,
                match=match,
            )

        # Update the match scores
        match.team1_score = team1_score
        match.team2_score = team2_score
        match.save()

    # Rotate teams for the next round
    teams.append(teams.pop(0))

    # Update the current date for the next weekend
    current_date += timedelta(days=7)

    # Increment the match week
    match_week += 1

    # Insert a bye week for each team after one match week
    if match_week == 2:
        teams.append(teams.pop(0))  # Rotate teams
        match_week = 0  # Reset the match week counter

print("Pro Rugby season matches and events with scores have been created.")
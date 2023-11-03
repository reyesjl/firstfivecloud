import random
from teams.models import Match, MatchEvent

MatchEvent.objects.all().delete()

# List of matches to simulate events for
matches = list(Match.objects.all())

# Define the match duration in minutes
match_duration = 80  # Adjust as needed for your game duration

# Define probabilities for different events
event_probabilities = {
    'try': 0.2,             # 20% chance of a try
    'try_conversion': 0.1,  # 10% chance of a try conversion
    'penalty_conversion': 0.15,  # 15% chance of a penalty conversion
    'penalty_try': 0.05,    # 5% chance of a penalty try
    'yellow_card': 0.05,   # 5% chance of a yellow card
    'red_card': 0.02,      # 2% chance of a red card
    'penalty': 0.3         # 30% chance of a penalty
}

for match in matches:
    # Initialize the scores for both teams
    team1_score = 0
    team2_score = 0

    # Simulate events during the match
    for minute in range(1, match_duration + 1):
        if random.random() < 0.1:  # Adjust the probability as needed
            # Randomly select an event based on probabilities
            event_type = random.choices(list(event_probabilities.keys()), weights=list(event_probabilities.values()))[0]
            
            # Convert QuerySets to lists and concatenate them
            all_players = list(match.team1.players.all()) + list(match.team2.players.all())
            player = random.choice(all_players)
            
            event = MatchEvent(
                event_type=event_type,
                minute=minute,
                player=player,
                match=match
            )
            event.save()

            # Update scores based on the selected event
            if event_type == 'try':
                if random.random() > 0.5:
                    team1_score += 5  # Team 1 scores a try
                else:
                    team2_score += 5  # Team 2 scores a try
            elif event_type == 'try_conversion':
                if random.random() > 0.5:
                    team1_score += 2  # Team 1 converts a try
                else:
                    team2_score += 2  # Team 2 converts a try
            elif event_type == 'penalty_conversion':
                if random.random() > 0.5:
                    team1_score += 3  # Team 1 converts a penalty
                else:
                    team2_score += 3  # Team 2 converts a penalty
            elif event_type == 'penalty_try':
                if random.random() > 0.5:
                    team1_score += 7  # Team 1 scores a penalty try
                else:
                    team2_score += 7  # Team 2 scores a penalty try

    # Update the match scores
    match.team1_score = team1_score
    match.team2_score = team2_score
    match.save()

    print(f"Match Result: {match.team1.name} {team1_score} - {team2_score} {match.team2.name}")

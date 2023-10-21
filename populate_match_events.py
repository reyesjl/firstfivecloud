import random
from teams.models import Match, MatchEvent 

# Function to create a random match event
def create_match_event(match, event_type, minute, player):
    return MatchEvent.objects.create(match=match, event_type=event_type, minute=minute, player=player)

# Fetch all matches
matches = Match.objects.all()

# Simulate match events for each match
for match in matches:
    for minute in range(1, 81):  # Simulate events for the first 80 minutes of a rugby match
        # Simulate random events with different probabilities
        if random.random() < 0.1:  # 10% chance of a 'try' scored
            player = f"Player {random.randint(1, 15)}"  # Random player number
            create_match_event(match, 'try', minute, player)
        elif random.random() < 0.05:  # 5% chance of a 'card' given
            player = f"Player {random.randint(1, 15)}"  # Random player number
            create_match_event(match, 'card', minute, player)
        elif random.random() < 0.1:  # 10% chance of a 'conversion'
            player = f"Player {random.randint(1, 15)}"  # Random player number
            create_match_event(match, 'conversion', minute, player)
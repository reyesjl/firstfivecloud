import random
from teams.models import Player

# Get all players
players = Player.objects.all()

# Define the desired time range in seconds for 10m and 40m sprints
min_10m_time = 4.0  # Minimum time for 10m sprint (in seconds)
max_10m_time = 5.0  # Maximum time for 10m sprint (in seconds)
min_40m_time = 6.5  # Minimum time for 40m sprint (in seconds)
max_40m_time = 7.5  # Maximum time for 40m sprint (in seconds)

# Loop through players and update 10m and 40m sprint times
for player in players:
    # Generate random sprint times within the specified ranges
    sprint_10m_time = round(random.uniform(min_10m_time, max_10m_time), 2)
    sprint_40m_time = round(random.uniform(min_40m_time, max_40m_time), 2)

    # Update the player's sprint times
    player.sprint_10m = sprint_10m_time
    player.sprint_40m = sprint_40m_time
    player.save()

    print(f"Updated 10m and 40m sprint times for {player.first_name} {player.last_name}")

print("Sprint time adjustment completed.")
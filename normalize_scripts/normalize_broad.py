import random
from teams.models import Player

# Get all players
players = Player.objects.all()

# Define the desired range for the broad jump in centimeters
min_broad_jump = 200  # Minimum broad jump distance (in centimeters)
max_broad_jump = 250  # Maximum broad jump distance (in centimeters)

# Loop through players and update broad jump distances
for player in players:
    # Generate a random broad jump distance within the specified range
    broad_jump_distance = random.randint(min_broad_jump, max_broad_jump)

    # Update the player's broad jump distance
    player.broad_jump = broad_jump_distance
    player.save()

    print(f"Updated broad jump distance for {player.first_name} {player.last_name}")

print("Broad jump adjustment completed.")
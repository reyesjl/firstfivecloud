import random
from teams.models import Player

# Get all players
players = Player.objects.all()

# Define the desired range for each attribute
# Update these values to set your desired ranges
min_chin_ups = 0
max_chin_ups = 15

min_back_squat = 50  # Minimum weight in kilograms
max_back_squat = 200  # Maximum weight in kilograms

min_trap_bar = 50  # Minimum weight in kilograms
max_trap_bar = 200  # Maximum weight in kilograms

# Loop through players and update the attributes
for player in players:
    # Generate random values within the specified ranges
    chin_ups = random.randint(min_chin_ups, max_chin_ups)
    back_squat = round(random.uniform(min_back_squat, max_back_squat), 2)
    trap_bar = round(random.uniform(min_trap_bar, max_trap_bar), 2)

    # Update the player's attributes
    player.chin_ups = chin_ups
    player.back_squat = back_squat
    player.trap_bar_deadlift = trap_bar
    player.save()

    print(f"Updated attributes for {player.first_name} {player.last_name}")

print("Attribute normalization completed.")
import random
from teams.models import Player

# Get all players
players = Player.objects.all()

# Define the desired time range in minutes
min_time_minutes = 270  # 4:30 in minutes
max_time_minutes = 330  # 5:30 in minutes

# Loop through players and update bronco time
for player in players:
    # Generate a random bronco time within the specified range
    random_time_minutes = random.randint(min_time_minutes, max_time_minutes)

    # Convert minutes back to hours and minutes format (HH:MM)
    hours = random_time_minutes // 60
    minutes = random_time_minutes % 60

    # Update the player's bronco time
    player.bronco_time = f"{hours:02d}:{minutes:02d}"
    player.save()

    print(f"Updated bronco time for {player.first_name} {player.last_name} to {player.bronco_time}")

print("Bronco time adjustment completed.")
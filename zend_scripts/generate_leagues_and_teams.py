from teams.models import League, Team, Player
import random

rugby_league_names = [
  "Super Rugby League",
  "Premier Rugby League",
  "Elite Rugby League",
  "National Rugby League",
  "Championship Rugby League",
  "All American Pro Rugby League",
  "International Rugby League",
  "Amateur Rugby League",
]

# Select a random league name
selected_league_name = "All American Pro"

# Check if the league already exists, or create it
league, created = League.objects.get_or_create(title=selected_league_name)

# Define a list of major cities on the East Coast as team names
cities = [
  "Plainsmen",
  "Blues",
  "United",
  "Steelers",
  "Capitals",
  "Admirals",
  "Raptors",
  "Mavericks",
  "Harmonics",
  "Phoenix",
  "Hornets"
]

# Shuffle the list
random.shuffle(cities)

for index, city in enumerate(cities, start=1):
  team_name = f"{city} RFC"
  team, created = Team.objects.get_or_create(
    name=team_name,
    league=league,
    crest="https://placehold.co/100x100",
    banner_image="https://placehold.co/1200x500",
    rank=index  # Pass the index directly as an integer
  )
  if created:
      print(f"Team '{team_name}' created successfully with rank {index}!")
  else:
      print(f"Team '{team_name}' already exists.")



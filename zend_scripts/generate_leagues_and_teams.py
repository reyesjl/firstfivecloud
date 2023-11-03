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
selected_league_name = random.choice(rugby_league_names)

# Check if the league already exists, or create it
league, created = League.objects.get_or_create(title=selected_league_name)

# Define a list of major cities on the East Coast as team names
cities = [
  "Alabama",
  "Alaska",
  "Arizona",
  "Arkansas",
  "California",
  "Colorado",
  "Connecticut",
  "Delaware",
  "Florida",
  "Georgia",
  "Hawaii",
  "Idaho",
  "Illinois",
  "Indiana",
  "Iowa",
  "Kansas",
  "Kentucky",
  "Louisiana",
  "Maine",
  "Maryland",
  "Massachusetts",
  "Michigan",
  "Minnesota",
  "Mississippi",
  "Missouri",
  "Montana",
  "Nebraska",
  "Nevada",
  "New Hampshire",
  "New Jersey",
  "New Mexico",
  "New York",
  "North Carolina",
  "North Dakota",
  "Ohio",
  "Oklahoma",
  "Oregon",
  "Pennsylvania",
  "Rhode Island",
  "South Carolina",
  "South Dakota",
  "Tennessee",
  "Texas",
  "Utah",
  "Vermont",
  "Virginia",
  "Washington",
  "West Virginia",
  "Wisconsin",
  "Wyoming"
]

# Shuffle the list and select the first 13 cities
random.shuffle(cities)
selected_cities = cities[:13]

for city in selected_cities:
  team_name = f"{city} RFC"
  team, created = Team.objects.get_or_create(
      name=team_name,
      league=league,
      crest="https://placehold.co/100x100",
      banner_image="https://placehold.co/1200x500",
  )
  if created:
      print(f"Team '{team_name}' created successfully!")
  else:
      print(f"Team '{team_name}' already exists.")


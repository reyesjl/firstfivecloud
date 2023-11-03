import random
from faker import Faker
from django.db import transaction
from teams.models import Team, Roster, Player
from datetime import datetime, timedelta

# Wipe the players and roster tables
Player.objects.all().delete()
Roster.objects.all().delete()

# Initialize the Faker instance
fake = Faker()

# Define a list of rugby positions
RUGBY_POSITIONS = [
    'Prop',
    'Hooker',
    'Prop',
    'Locke',
    'Locke',
    'Flanker',
    'Flanker',
    'Number Eight',
    'Half-Back',
    'Fly-Half',
    'Center',
    'Center',
    'Wing',
    'Wing',
    'Full-Back',
]

# Specify the number of players you want to create for each team
num_starting_players_per_team = 23
num_reserve_players_per_team = 25

# Get all the teams
teams = Team.objects.all()

# Create one roster for each team
with transaction.atomic():
    for team in teams:
        # Create a roster for the team
        roster, created = Roster.objects.get_or_create(team=team)

        for i in range(num_starting_players_per_team):
            # Generate a fake name
            first_name = fake.first_name()
            last_name = fake.last_name()

            # Use the predefined rugby positions for the first 15 players
            if i < len(RUGBY_POSITIONS):
                position = RUGBY_POSITIONS[i]
            else:
                # Randomly select a position for additional players
                position = random.choice(RUGBY_POSITIONS)

            height = random.randint(160, 200)
            weight = random.randint(60, 120)

            # Calculate date of birth within the range of 18 to 35 years
            today = datetime.now()
            max_age_days = 35 * 365  # Maximum age in days
            min_age_days = 18 * 365  # Minimum age in days
            birthdate = today - timedelta(days=random.randint(min_age_days, max_age_days))

            # Create a player with the generated data
            player = Player(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=birthdate.date(),
                position=position,
                height=height,
                weight=weight,
                speed=random.randint(60, 100),
                strength=random.randint(60, 100),
                agility=random.randint(60, 100),
                endurance=random.randint(60, 100),
                tackling=random.randint(60, 100),
                passing=random.randint(60, 100),
                kicking=random.randint(60, 100),
                team=team,  # Assign the player to the team
            )

            player.save()

            # Add the player to the roster
            roster.starting_23.add(player)

        for _ in range(num_reserve_players_per_team):
            # Generate a fake name
            first_name = fake.first_name()
            last_name = fake.last_name()

            # Randomly select a position for reserve players
            position = random.choice(RUGBY_POSITIONS)

            height = random.randint(160, 200)
            weight = random.randint(60, 120)

            # Calculate date of birth within the range of 18 to 35 years
            today = datetime.now()
            max_age_days = 35 * 365  # Maximum age in days
            min_age_days = 18 * 365  # Minimum age in days
            birthdate = today - timedelta(days=random.randint(min_age_days, max_age_days))

            # Create a player with the generated data
            player = Player(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=birthdate.date(),
                position=position,
                height=height,
                weight=weight,
                speed=random.randint(60, 100),
                strength=random.randint(60, 100),
                agility=random.randint(60, 100),
                endurance=random.randint(60, 100),
                tackling=random.randint(60, 100),
                passing=random.randint(60, 100),
                kicking=random.randint(60, 100),
                team=team,  # Assign the player to the team
            )

            player.save()

            # Add the player to the roster
            roster.reserves.add(player)


import random
from teams.models import Player  # Import your Player model from your Django app

Player.objects.all().delete()

# Define common rugby first names and last names
common_first_names = [
  "John", "James", "Michael", "David", "William", "Richard", "Thomas", "Matthew", "Andrew", "Christopher",
  "Joseph", "Robert", "Daniel", "Paul", "Peter", "Benjamin", "Stephen", "Jonathan", "George", "Charles",
  "Samuel", "Nicholas", "Anthony", "Martin", "Edward", "Patrick", "Henry", "Alexander", "Philip", "Simon",
  "Lawrence", "Donald", "Joseph", "Mark", "Timothy", "Jeffrey", "Kenneth", "Brian", "Gregory", "Jason",
  "Nathaniel", "Lawrence", "Timothy", "Kenneth", "Jonathan", "Roger", "Adam", "Larry", "Roger", "Edward",
  "Eric", "Jeffrey", "Roy", "Vincent", "Howard", "Curtis", "Steve", "Philip", "Nicholas", "Alan", "Eugene",
  "Carl", "Keith", "Gerald", "Clarence", "Ralph", "Glenn", "Lester", "Duane", "Frederick", "Lee", "Glen",
  "Gilbert", "Ron", "Johnnie", "Ivan", "Lewis", "Ray", "Norman", "Marvin", "Eugene", "Bradley", "Tom",
  "Dwayne", "Garry", "Glenn", "Jeffery", "Warren", "Franklin", "Gerard", "Wallace", "Allan", "Vernon",
  "Freddie", "Antonio", "Oscar", "Jay", "Vernon", "Leo", "Roberto", "Rex", "Chris", "Shawn", "Ricardo"
]

common_last_names = [
  "Smith", "Williams", "Jones", "Taylor", "Brown", "Johnson", "Wilson", "Davies", "Evans", "Thomas",
  "Roberts", "James", "Edwards", "Harris", "Davis", "Morgan", "Patel", "Lee", "Lewis", "Clark",
  "Walker", "White", "Hall", "Green", "Martin", "Wright", "Jackson", "Hill", "Allen", "Wood",
  "Turner", "Lewis", "Harrison", "Scott", "Young", "Morris", "King", "Ward", "Cook", "Bailey",
  "Murphy", "Miller", "Cooper", "Murray", "Reed", "Baker", "Ward", "Phillips", "Mitchell", "Carter",
  "Cox", "Owen", "Dixon", "Ellis", "Henry", "Hughes", "Graham", "Simpson", "Day", "Knight",
  "Stevens", "Fox", "Webb", "Grant", "Russell", "Thompson", "Rose", "Ford", "Mason", "Foster",
  "Andrews", "Hunter", "Gibson", "O'Neill", "Pearce", "Holland", "Stewart", "Burns", "Bradley",
  "Turner", "Richardson", "Black", "Holmes", "Porter", "Dunn", "Spencer", "Hayes", "Kim", "Riley",
  "Smith", "Lee", "Clarke", "Ho", "Ahmed", "Kaur", "Mccarthy", "Boyd", "Adams", "Khan", "Yates",
  "Kumar", "Armstrong", "Wong", "Wilkinson", "Lynch", "Johnson", "Sullivan", "Bell", "Rees", "Gould"
]

# List of rugby positions with weight based on the desired distribution
positions = [
    ('PR', 3),   # Prop
    ('HK', 2),   # Hooker
    ('LK', 4),   # Locke
    ('FL', 4),   # Flanker
    ('N8', 3),   # Number Eight
    ('SH', 3),   # Half-Back
    ('FH', 3),   # Fly-Half
    ('CE', 4),   # Center
    ('WI', 4),   # Wing
    ('FB', 3)    # Full-Back
]

# Generate and save random players
player_count = 13 * 40  # 13 teams with 40 players each
halfback_count = 13 * 3  # 13 teams with 3 halfbacks each
flyhalf_count = 13 * 3  # 13 teams with 3 fly-halves each

for _ in range(player_count):
    # Select a position with weight-based distribution
    position = random.choices([pos[0] for pos in positions], weights=[pos[1] for pos in positions])[0]

    # If it's a halfback, check if the limit is reached
    if position == 'SH' and halfback_count <= 0:
        position = random.choice([pos[0] for pos in positions if pos[0] != 'SH'])
    elif position == 'FH' and flyhalf_count <= 0:
        position = random.choice([pos[0] for pos in positions if pos[0] != 'FH'])

    # Decrement the counts for halfbacks and fly-halves
    if position == 'SH':
        halfback_count -= 1
    elif position == 'FH':
        flyhalf_count -= 1

    # Generate random attributes for the player
    first_name = random.choice(common_first_names)
    last_name = random.choice(common_last_names)
    date_of_birth = "2000-01-01"
    height = random.randint(170, 200)
    weight = random.randint(70, 120)

    # Generate random attributes for player ratings
    speed = random.randint(70, 100)
    strength = random.randint(70, 100)
    agility = random.randint(70, 100)
    endurance = random.randint(70, 100)
    tackling = random.randint(70, 100)
    passing = random.randint(70, 100)
    kicking = random.randint(70, 100)

    # Generate random attributes for additional attributes
    bronco_time = round(random.uniform(12.0, 16.0), 2)
    sprint_10m = round(random.uniform(3.0, 4.0), 2)
    sprint_40m = round(random.uniform(6.0, 8.0), 2)
    broad_jump = random.randint(200, 300)
    chin_ups = random.randint(5, 20)
    back_squat = random.randint(100, 200)
    trap_bar_deadlift = random.randint(100, 200)

    # Create and save the player
    player = Player(
        first_name=first_name,
        last_name=last_name,
        date_of_birth=date_of_birth,
        position=position,
        height=height,
        weight=weight,
        speed=speed,
        strength=strength,
        agility=agility,
        endurance=endurance,
        tackling=tackling,
        passing=passing,
        kicking=kicking,
        bronco_time=bronco_time,
        sprint_10m=sprint_10m,
        sprint_40m=sprint_40m,
        broad_jump=broad_jump,
        chin_ups=chin_ups,
        back_squat=back_squat,
        trap_bar_deadlift=trap_bar_deadlift,
        # Leave the team field as blank
    )
    player.save()


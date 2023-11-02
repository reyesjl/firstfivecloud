from django.db import models

class League(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    year_founded = models.IntegerField(blank=True, null=True)
    founders = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=100)
    crest = models.CharField(max_length=200, blank=True)
    banner_image = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    founded_in = models.PositiveIntegerField(null=True, blank=True)
    division = models.CharField(max_length=100, blank=True)
    rank = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='teams', blank=True, null=True)

    def __str__(self):
        location_info = f"{self.city}, {self.state}" if self.city and self.state else "Location Unknown"
        founded_info = f"Founded in {self.founded_in}" if self.founded_in else "Founding Year Unknown"
        return f"{self.name} ({location_info}) - {founded_info}"
    
    class Meta:
        verbose_name = "Rugby Team"       # Singular name for the model
        verbose_name_plural = "Rugby Teams"  # Plural name for the model
    
class Match(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_as_team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_as_team2')
    team1_score = models.IntegerField(default=0)  # Score for team 1
    team2_score = models.IntegerField(default=0)  # Score for team 2

    def __str__(self):
        return f"{self.date} - {self.team1.name} {self.team1_score} vs {self.team2_score} {self.team2.name}"
    
    class Meta:
        verbose_name = "Match"       # Singular name for the model
        verbose_name_plural = "Matches"  # Plural name for the model

class MatchEvent(models.Model):
    EVENT_TYPES = (
        ('try', 'Try Scored'),
        ('yellow_card', 'Yellow Card Given'),
        ('red_card', 'Red Card Given'),
        ('try_conversion', 'Try Conversion'),
        ('penalty_conversion', 'Penalty Conversion'),
        ('penalty_try', 'Penalty Try')
    )
    event_type = models.CharField(max_length=18, choices=EVENT_TYPES)
    minute = models.PositiveSmallIntegerField()
    player = models.CharField(max_length=100)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return f"{self.event_type} at {self.minute}' by {self.player}"
    
class Player(models.Model):
    # Define choices for rugby positions
    RUGBY_POSITIONS = (
        ('PR', 'Prop'),
        ('HK', 'Hooker'),
        ('LK', 'Locke'),
        ('FL', 'Flanker'),
        ('N8', 'Number Eight'),
        ('SH', 'Half-Back'),
        ('FH', 'Fly-Half'),
        ('CE', 'Center'),
        ('WI', 'Wing'),
        ('FB', 'Full-Back'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    position = models.CharField(max_length=13, choices=RUGBY_POSITIONS)
    height = models.PositiveIntegerField()  # Height in centimeters
    weight = models.PositiveIntegerField()  # Weight in kilograms
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players', null=True, blank=True)

    # Additional attributes for player ratings
    speed = models.PositiveSmallIntegerField(null=True, blank=True)
    strength = models.PositiveSmallIntegerField(null=True, blank=True)
    agility = models.PositiveSmallIntegerField(null=True, blank=True)
    endurance = models.PositiveSmallIntegerField(null=True, blank=True)
    tackling = models.PositiveSmallIntegerField(null=True, blank=True)
    passing = models.PositiveSmallIntegerField(null=True, blank=True)
    kicking = models.PositiveSmallIntegerField(null=True, blank=True)

    # Additional attributes
    bronco_time = models.CharField(max_length=5, null=True, blank=True)
    sprint_10m = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sprint_40m = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    broad_jump = models.PositiveIntegerField(null=True, blank=True)
    chin_ups = models.PositiveSmallIntegerField(null=True, blank=True)
    back_squat = models.PositiveIntegerField(null=True, blank=True)
    trap_bar_deadlift = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"

    class Meta:
        verbose_name = "Rugby Player"
        verbose_name_plural = "Rugby Players"

class Roster(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='roster')
    starting_23 = models.ManyToManyField(Player, related_name='roster_starting_23', blank=True)
    reserves = models.ManyToManyField(Player, related_name='roster_reserves', blank=True)

    def __str__(self):
        return f"Roster for {self.team.name}"

    class Meta:
        verbose_name = "Roster"
        verbose_name_plural = "Rosters"

from django.db import models

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
    league = models.CharField(max_length=100, blank=True)

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
        return f"{self.date} - {self.team1} {self.team1_score} vs {self.team2_score} {self.team2}"

class MatchEvent(models.Model):
    EVENT_TYPES = (
        ('try', 'Try Scored'),
        ('card', 'Card Given'),
        ('conversion', 'Conversion'),
    )
    event_type = models.CharField(max_length=10, choices=EVENT_TYPES)
    minute = models.PositiveSmallIntegerField()
    player = models.CharField(max_length=100)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return f"{self.event_type} at {self.minute}' by {self.player}"

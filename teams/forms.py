# Filename: teams/forms.py

from django import forms
from .models import League, Team, Player, League, MatchEvent, Match

class MatchFilterForm(forms.Form):
  league = forms.ModelMultipleChoiceField(
    queryset=League.objects.all(),
    widget=forms.CheckboxSelectMultiple,
    required=False
  )

class PlayerForm(forms.ModelForm):
  class Meta:
    model = Player
    fields = '__all__'

class TeamForm(forms.ModelForm):
  class Meta:
    model = Team
    exclude = ['coach']

class MatchForm(forms.ModelForm):
  class Meta:
    model = Match
    fields = '__all__'

class MatchEventForm(forms.ModelForm):
  class Meta:
    model = MatchEvent
    fields = '__all__'

class LeagueForm(forms.ModelForm):
  class Meta:
    model = League
    fields = '__all__'
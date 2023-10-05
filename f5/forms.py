from django import forms
from .models import EventTicket

class EventTicketForm(forms.ModelForm):
    class Meta:
        model = EventTicket
        fields = ['player_full_name', 'player_age', 'player_grade', 'parent_full_name', 'parent_email', 'risk_checkbox']
        help_texts = {
            'risk_checkbox': 'By checking this box, I acknowledge and accept all risks, including but not limited to injuries, associated with participating in rugby, sports activities, and officiating. I understand that I am solely responsible for my own safety and well-being.',
        }
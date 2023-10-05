from django import forms
from .models import EventTicket

class EventTicketForm(forms.ModelForm):
    class Meta:
        model = EventTicket
        fields = ['player_full_name', 'player_age', 'player_grade', 'parent_full_name', 'parent_email', 'risk_checkbox']
        help_texts = {
            'risk_checkbox': 'I acknowledge that there are certain risks inherent in this program, as with all physical activity. I acknowledge that all risks cannot be prevented and I assume those risks beyond the control of the staff. I represent that my minor child is able, with or without accommodation, to participate in this program, and has obtained any required immunizations. Should my minor child require emergency medical treatment as a result of accident or illness arising during the activity, I consent to such treatment. I acknowledge that the staff I does not provide health and accident insurance and I agree to be financially responsible for any medical bills incurred as a result of emergency medical treatment. I will notify the activity leader in writing if my minor child has medical conditions about which emergency medical personnel should be informed.',
        }
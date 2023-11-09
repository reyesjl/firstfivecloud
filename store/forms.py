# members/forms.py

from django import forms
from .models import CapsInquiry

class CapsInquiryForm(forms.ModelForm):
    class Meta:
        model = CapsInquiry
        fields = ['email', 'team_name', 'cap_base_color', 'cap_trim_color', 'cell_phone_number', 'number_of_caps']
        help_texts = {
            'cell_phone_number': 'We will contact you to confirm details regarding the order.',
            'number_of_caps': 'How many caps will you be ordering?',
        }
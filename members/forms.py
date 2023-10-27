# members/forms.py

from django import forms
from .models import FirstfiveUser

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
    class Meta:
        model = FirstfiveUser
        fields = ['username', 'password', 'email', 'bio']
        help_texts = {
            'password': 'secret safe',
            'email': 'please ensure you can login to this email',
            'bio': 'type something about you',
        }

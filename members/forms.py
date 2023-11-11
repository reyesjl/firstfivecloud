# members/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import FirstfiveUser
from f5.models import Event, EventTicket

class FFRLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}),
        label='',
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        label=''
    )
    
    class Meta:
        model = FirstfiveUser
        fields = ['username', 'password']

class FFRSignupForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}),
        label='',
        help_text='Your username should be unique and contain only letters, numbers, and @/./+/-/_ characters.'
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your email address'}),
        label='',
        help_text='Enter a valid email address please.'
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        label='',
        help_text='Must be at-least 8 characters long and be uncommon.'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
        label='',
        help_text='Re-enter your password. Save it someplace.'
    )
    class Meta:
        model = FirstfiveUser
        fields = ['username', 'email', 'password1', 'password2']

class AlterUserForm(forms.ModelForm):
    class Meta:
        model = FirstfiveUser
        fields = ['email', 'profile_photo', 'bio',]

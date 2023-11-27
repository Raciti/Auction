# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Obbligatorio. Inserisci un indirizzo email valido.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Il tuo Nome')
    last_name = forms.CharField(max_length=30, required=True, help_text='Il tuo Cognome')

    class Meta:
        proxy = True
        model = User
        fields = ( 'email', 'username','first_name', 'last_name', 'password1', 'password2')

from django.contrib.auth.forms import AuthenticationForm
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')

from django.contrib.auth.forms import PasswordResetForm
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email'}))
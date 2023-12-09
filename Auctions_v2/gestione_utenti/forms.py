from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms



class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Obbligatorio. Inserisci un indirizzo email valido.')
    username = forms.CharField(max_length=30, required=True, help_text='Il tuo Nome')
    first_name = forms.CharField(max_length=30, required=True, help_text='Il tuo Nome')
    last_name = forms.CharField(max_length=30, required=True, help_text='Il tuo Cognome')

    class Meta:
        proxy = True
        model = get_user_model()
        fields = ('email', 'username','first_name', 'last_name', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')

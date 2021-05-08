from django.forms import TextInput, PasswordInput, CharField

from .models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    """New user registration form"""
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

    class Meta:
        model = User
        fields = ('username',)
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nickname'
            })
        }

from django.forms import TextInput, PasswordInput, CharField, ModelForm, Textarea, CheckboxSelectMultiple

from .models import User, Article, Comment
from django.contrib.auth.forms import UserCreationForm


class ArticleForm(ModelForm):
    """Article form"""
    class Meta:
        model = Article
        fields = ('title', 'text', 'tags')
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control'
            }),
            'text': Textarea(attrs={
                'class': 'form-control'
            }),
            'tags': CheckboxSelectMultiple()
        }


class RegistrationForm(UserCreationForm):
    """User registration form"""
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


class CommentForm(ModelForm):
    """Article comment form"""

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control'
            })
        }

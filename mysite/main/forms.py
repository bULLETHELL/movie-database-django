from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.backends import AllowAllUsersModelBackend
from django import forms
from django.forms import widgets, ModelForm
from django.forms.widgets import TextInput, PasswordInput

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'USERNAME'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'PASSWORD'}))

class DiscussionForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()
    author = forms.CharField()
    parent_movie = forms.CharField()

class CommentForm(forms.Form):
    text = forms.CharField()
    author = forms.CharField()
    parent_discussion = forms.CharField()

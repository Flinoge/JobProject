from django import forms
from django.forms import ModelForm
from .models import PlayersModel


class SignupForm(forms.Form):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)


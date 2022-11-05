from dataclasses import fields
from gzip import FNAME
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    first_name=forms.CharField(max_length=100,required=True)
    last_name=forms.CharField(max_length=100,required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class ItemCreationForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['seller', 'buyer', 'current_bid', 'date_created', 'tags']




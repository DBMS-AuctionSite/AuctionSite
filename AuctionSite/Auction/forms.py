from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class SellerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class AuctionCreationForm(ModelForm):
    class Meta:
        model = Auction
        fields = '__all__'
        exclude = ['seller', 'finalbid', 'soldto']


class ItemCreationForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['seller', 'date_created', 'tags']

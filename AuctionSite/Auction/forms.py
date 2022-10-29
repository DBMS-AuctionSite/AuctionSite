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


class ItemCreationForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['seller', 'buyer', 'current_bid', 'date_created', 'tags']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'minimum_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'item_pic': forms.ImageField(attrs={'class': 'form-control'}),

        }

# class CustomerForm(ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'
#         exclude = ['user']


# class SellerForm(ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'
#         exclude = ['user']


# class AuctionCreationForm(ModelForm):
#     class Meta:
#         model = Auction
#         fields = '__all__'
#         exclude = ['seller', 'finalbid', 'soldto']

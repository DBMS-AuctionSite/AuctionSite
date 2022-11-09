from email.policy import default
from pyexpat import model
from tokenize import blank_re
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Item(models.Model):
    seller = models.ForeignKey(
        User, null=True, related_name='seller', on_delete=models.CASCADE)
    buyer = models.ForeignKey(
        User, null=True, related_name='buyer', blank=True, on_delete=models.SET_NULL)

    CATEGORY = (
        ('Electronics', 'Electronics'),
        ('Sports', 'Sports'),
        ('Household', 'Household'),
        ('Clothing', 'Clothing'),
        ('Footwear', 'Footwear'),
        ('Cosmetics', 'Cosmetics'),
        ('Other', 'Other')
    )
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    minimum_price = models.PositiveIntegerField(default=0)
    current_bid = models.PositiveBigIntegerField(blank=True, null=True, default=0)
    duration = models.PositiveBigIntegerField(default=8)
    item_pic = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name


class Bid(models.Model):
    Item = models.ForeignKey(Item, on_delete=models.CASCADE)
    Bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    Bid = models.PositiveIntegerField()
    # for status True: winning
    Status = models.BooleanField()

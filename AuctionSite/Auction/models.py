from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Seller(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    CATEGORY = (
        ('Electronics', 'Electronics'),
        ('Sports', 'Sports'),
        ('Household', 'Household'),
        ('Clothing', 'Clothing'),
        ('Footwear', 'Footwear'),
        ('Cosmetics', 'Cosmetics')
    )
    name = models.CharField(max_length=200, null=True)
    seller = models.OneToOneField(
        Seller, null=True, blank=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    initialBid = models.IntegerField(default=0, null=False)
    tags = models.ManyToManyField(Tag)
    item_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Auction(models.Model):
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    duration = models.IntegerField()
    finalbid = models.IntegerField(default=0)
    soldto = models.OneToOneField(
        Customer, null=True, blank=True, on_delete=models.CASCADE)

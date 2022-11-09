from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
import json

# Create your views here.


# @login_required(login_url='login')
def home(request):
    items = Item.objects.all()
    print(len(items)) #console output for debugging
    context = {'items': items}
    return render(request, "Auction/home.html", context)


def registerPage(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'registration/register.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profilePage(request):
    context = {}
    return render(request, 'Auction/profile.html', context)


@login_required(login_url='login')
def sellPage(request):
    form = ItemCreationForm()
    if request.method == 'POST':
        form = ItemCreationForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.seller = request.user
        post.save()
        messages.success(request, f"{post.name} was added to the auction")
        return redirect("/")

    context = {'form': form}
    return render(request, 'Auction/sell.html', context)


def add_bid(request, pk):
    order = Item.objects.get(id=pk)
    current_bid = order.current_bid
    if request.method == "POST":
        form = BidForm(request.POST, instance=order)
        if form.is_valid():
            bid = int(form.cleaned_data['current_bid'])
            if (current_bid == None and bid >= order.minimum_price):
                form.save()

            elif (bid >= order.minimum_price and bid > current_bid):
                form.save()

            else:
                messages.error(request, "Please enter a valid bid")

            return HttpResponse(
                status=204)
        # return redirect("/")
    else:
        form = BidForm(instance=order)
    return render(request, 'bid_form.html', {
        'form': form,
    })

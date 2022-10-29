from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.


@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, "Auction/home.html", context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'Auction/login.html', context)


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'Auction/register.html', context)


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
        form = ItemCreationForm(request.POST)
        post = form.save(commit=False)
        post.seller = request.user
        post.save()
        messages.success(request, f"{post.name} was added to the auction")
        return redirect("/")

    context = {'form': form}
    return render(request, 'Auction/sell.html', context)

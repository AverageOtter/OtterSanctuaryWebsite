from turtle import title
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from . import models, forms
from django.contrib import messages

# Create your views here.
def index(request):
    current_user = request.user
    context = {
        "title": "Otter Region",
        "current_user": current_user,
    }
    return render(request, "index.html", context=context)


def aboutUs(request):
    current_user = request.user
    context = {
        "title": "Otter Staff",
        "current_user": current_user,
    }
    return render(request, "aboutus.html", context=context)


def otterDB(request):
    current_user = request.user
    context = {
        "title": "Otter Den",
        "current_user": current_user,
    }
    return render(request, "otterDB.html", context=context)


@login_required
def chat(request):
    current_user = request.user
    context = {
        "title": "Chat",
        "current_user": current_user,
    }
    return render(request, "chat.html", context=context)


def chatEmp(request):
    current_user = request.user
    context = {
        "title": "Chat Elevated",
        "current_user": current_user,
    }
    return render(request, "chatEmp.html", context=context)


def game(request):
    current_user = request.user
    context = {
        "title": "Game",
        "current_user": current_user,
    }
    return render(request, "game.html", context=context)


def register(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect("/login/")

    else:
        form = forms.RegistrationForm(request.POST)
    context = {"form": form}
    return render(request, "registration/register.html", context=context)


def logout_user(request):
    logout(request)
    return redirect("/login/")


#! Remove after pages have been setup
def ex(request):
    current_user = request.user
    context = {
        "title": "Example",
        "current_user": current_user,
    }
    return render(request, "FoundationEx.html", context=context)

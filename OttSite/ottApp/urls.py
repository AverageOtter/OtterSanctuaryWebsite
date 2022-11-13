from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("aboutus/", views.aboutUs, name="aboutUs"),
    path("otterDB/", views.otterDB, name="otterDB"),
    path("chat/", views.chat, name="chat"),
    path("login/", auth_views.LoginView.as_view()),
    path("register/", views.register),
    path("FoundationEx/", views.ex, name="FoundationEx"),
    path("game", views.game, name="game"),  #!Remove
    path("logout/", views.logout_user),
]

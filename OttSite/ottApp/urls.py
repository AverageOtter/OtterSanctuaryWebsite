from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('FoundationEx', views.ex, name='FoundationEx'), #!Remove
]
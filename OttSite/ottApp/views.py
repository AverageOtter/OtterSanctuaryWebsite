from turtle import title
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "title" : "Otter Den",
    }
    return render(request, "index.html", context=context)

#! Remove after pages have been setup
def ex(request):
    context = {
        "title" : "Otter Den",
    }
    return render(request, "FoundationEx.html", context=context)
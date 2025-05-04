from django.shortcuts import render
from django.views.generic import ListView
from .models import Bug


# Create your views here.
class BugTrackerListView(ListView):
    model = Bug
    template_name = "home.html"

from django.shortcuts import render
from django.views.generic import ListView

from .models import Bug


class BugListView(ListView):
    model = Bug
    template_name = "dashboard.html"

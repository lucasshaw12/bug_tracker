from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.views import View

from .models import Bug


class BugListView(ListView):
    model = Bug
    template_name = "dashboard.html"


class BugCreateView(CreateView):
    model = Bug
    fields = [
        "bug_title",
        "bug_description",
        "application_name",
        "expected_behaviour",
        "actual_behaviour",
        "user_assigned_to",
        "completion_status",
        "complexity_level",
        "severity_level",
    ]
    template_name = "bugs/bug_form.html"
    success_url = reverse_lazy("dashboard")


class BugUpdateView(UpdateView):
    model = Bug
    fields = BugCreateView.fields
    template_name = "bugs/bug_form.html"
    success_url = reverse_lazy("dashboard")


class BugCompleteView(View):
    def post(self, request, pk):
        bug = get_object_or_404(Bug, pk=pk)
        bug.completion_status = "Fixed"
        bug.completed_on = timezone.now()
        bug.save()
        return redirect("dashboard")


class BugCloseView(View):
    def post(self, request, pk):
        bug = get_object_or_404(Bug, pk=pk)
        bug.completion_status = "Closed without fix"
        bug.completed_on = timezone.now()
        bug.save()
        return redirect("dashboard")

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Bug


class BugListView(LoginRequiredMixin, ListView):
    model = Bug
    template_name = "dashboard.html"
    login_url = reverse_lazy("login")

    def get_queryset(self):
        return Bug.objects.order_by("date_raised")


class BugCreateView(LoginRequiredMixin, CreateView):
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
    login_url = reverse_lazy("login")


class BugUpdateView(LoginRequiredMixin, UpdateView):
    model = Bug
    fields = BugCreateView.fields
    template_name = "bugs/bug_form.html"
    success_url = reverse_lazy("dashboard")
    login_url = reverse_lazy("login")


class BugDeleteView(LoginRequiredMixin, DeleteView):
    model = Bug
    template_name = "bugs/bug_confirm_delete.html"
    success_url = reverse_lazy("dashboard")
    login_url = reverse_lazy("login")


@method_decorator(login_required(login_url=reverse_lazy("login")), name="dispatch")
class BugCompleteView(View):
    def post(self, request, pk):
        bug = get_object_or_404(Bug, pk=pk)
        bug.completion_status = "Fixed"
        bug.completed_on = timezone.now()
        bug.save()
        return redirect("dashboard")


@method_decorator(login_required(login_url=reverse_lazy("login")), name="dispatch")
class BugCloseView(View):
    def post(self, request, pk):
        bug = get_object_or_404(Bug, pk=pk)
        bug.completion_status = "Closed without fix"
        bug.completed_on = timezone.now()
        bug.save()
        return redirect("dashboard")

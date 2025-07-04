from django.db import models
from django.urls import reverse

from django.conf import settings


# Create your models here.
class Bug(models.Model):
    STATUS_CHOICES = {
        ("Not started", "Not started"),
        ("In progress", "In progress"),
        ("Blocked", "Blocked"),
        ("Under peer review", "Under peer review"),
        ("Fixed", "Fixed"),
        ("Closed without fix", "Closed without fix"),
    }
    bug_title = models.CharField(max_length=40)
    bug_description = models.TextField()
    application_name = models.CharField(max_length=40)
    expected_behaviour = models.TextField()
    actual_behaviour = models.TextField()
    user_assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )  # settings.AUTH_USER_MODEL is used for the Custom User
    completion_status = models.CharField(max_length=40, choices=STATUS_CHOICES)
    complexity_level = models.PositiveSmallIntegerField()
    severity_level = models.PositiveSmallIntegerField()
    date_raised = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bug_title

    def status_class(self):
        if self.completion_status == "Fixed":
            return "bg-success text-white"
        elif self.completion_status == "Closed without fix":
            return "bg-secondary text-white"
        else:
            return ""

    def is_complete_status_class(self):
        if self.completion_status in ("Fixed", "Closed without fix"):
            return "text-white btn-outline-light"
        else:
            return "text-danger btn-outline-danger"

    def is_closed(self):
        if (
            self.completion_status == "Fixed"
            or self.completion_status == "Closed without fix"
        ):
            return True

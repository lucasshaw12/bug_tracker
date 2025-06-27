from django import forms
from .models import Bug

class BugForm(forms.ModelForm):
    class Meta:
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

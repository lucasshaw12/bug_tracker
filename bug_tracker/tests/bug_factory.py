from django.contrib.auth import get_user_model
from bug_tracker.models import Bug


def open_bug_data(user):
    return {
        "bug_title": "Sample Open Bug",
        "bug_description": "A test bug",
        "application_name": "TestApp",
        "expected_behaviour": "Should work",
        "actual_behaviour": "Doesn't work",
        "user_assigned_to": user.pk,
        "completion_status": "Not started",
        "complexity_level": 1,
        "severity_level": 1,
    }


def complete_bug_data(user):
    data = open_bug_data(user)
    data["bug_title"] = "Sample Complete Bug"
    data["completion_status"] = "Fixed"
    return data


def closed_bug_data(user):
    data = open_bug_data(user)
    data["bug_title"] = "Sample Closed Bug"
    data["completion_status"] = "Closed without fix"
    return data

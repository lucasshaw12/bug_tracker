from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from bug_tracker.models import Bug


class BugDeleteTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="deleter", email="deleter@example.com", password="DeleteMe123!"
        )
        self.bug_data = {
            "bug_title": "Bug to Delete",
            "bug_description": "This bug will be deleted",
            "application_name": "MyApp",
            "expected_behaviour": "Should work",
            "actual_behaviour": "Doesn't work",
            "user_assigned_to": self.user,
            "completion_status": "Not started",
            "complexity_level": 1,
            "severity_level": 1,
        }
        self.create_bug = partial(Bug.objects.create, **self.bug_data)
        self.bug = self.create_bug()

    def delete(self):
        return self.client.post(reverse("bug_delete", kwargs={"pk": self.bug.pk}))

    def test_delete_bug_redirects(self):
        response = self.delete()
        self.assertRedirects(response, reverse("dashboard"))

    def test_delete_bug_removes_object(self):
        self.delete()
        exists = Bug.objects.filter(pk=self.bug.pk).exists()
        self.assertFalse(exists)

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from bug_tracker.models import Bug


class BugEditTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="devuser", email="dev@example.com", password="DevPass123!"
        )
        self.bug = Bug.objects.create(
            bug_title="Initial Bug",
            bug_description="Initial description",
            application_name="MyApp",
            expected_behaviour="Expect X",
            actual_behaviour="Does Y",
            user_assigned_to=self.user,
            completion_status="Not started",
            complexity_level=1,
            severity_level=1,
        )
        self.update_data = {
            "bug_title": "Updated Bug",
            "bug_description": self.bug.bug_description,
            "application_name": self.bug.application_name,
            "expected_behaviour": self.bug.expected_behaviour,
            "actual_behaviour": self.bug.actual_behaviour,
            "user_assigned_to": self.user.pk,
            "completion_status": "Fixed",
            "complexity_level": 2,
            "severity_level": 2,
        }
        self.invalid_update = self.update_data.copy()
        self.invalid_update["complexity_level"] = -5

    def test_get_edit_view(self):
        response = self.client.get(reverse("bug_edit", kwargs={"pk": self.bug.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Initial Bug")

    def test_edit_with_valid_data(self):
        response = self.client.post(
            reverse("bug_edit", kwargs={"pk": self.bug.pk}), self.update_data
        )
        self.assertEqual(response.status_code, 302)
        self.bug.refresh_from_db()
        self.assertEqual(self.bug.bug_title, "Updated Bug")
        self.assertEqual(self.bug.completion_status, "Fixed")

    def test_edit_with_invalid_data(self):
        response = self.client.post(
            reverse("bug_edit", kwargs={"pk": self.bug.pk}), self.invalid_update
        )
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertIn("complexity_level", form.errors)

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from bug_tracker.models import Bug


class BugCreateTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="devuser", email="dev@example.com", password="DevPass123!"
        )
        self.valid_data = {
            "bug_title": "Sample Bug",
            "bug_description": "Something isn’t working",
            "application_name": "MyApp",
            "expected_behaviour": "Should do X",
            "actual_behaviour": "Does Y",
            "user_assigned_to": self.user.pk,
            "completion_status": "Not started",
            "complexity_level": 2,
            "severity_level": 3,
        }
        # invalid cases
        self.invalid_missing_title = self.valid_data.copy()
        self.invalid_missing_title.pop("bug_title")
        self.invalid_bad_status = self.valid_data.copy()
        self.invalid_bad_status["completion_status"] = "Unknown status"
        self.invalid_bad_complexity = self.valid_data.copy()
        self.invalid_bad_complexity["complexity_level"] = -1

    def test_get_create_view(self):
        response = self.client.get(reverse("bug_add"))
        self.assertEqual(response.status_code, 200)

    def test_create_with_valid_data(self):
        response = self.client.post(reverse("bug_add"), self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Bug.objects.count(), 1)
        bug = Bug.objects.first()
        self.assertEqual(bug.bug_title, "Sample Bug")
        self.assertEqual(bug.completion_status, "Not started")

    def test_create_missing_title_fails(self):
        response = self.client.post(reverse("bug_add"), self.invalid_missing_title)
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertIn("bug_title", form.errors)

    def test_create_invalid_status_fails(self):
        response = self.client.post(reverse("bug_add"), self.invalid_bad_status)
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertIn("completion_status", form.errors)

    def test_create_invalid_complexity_fails(self):
        response = self.client.post(reverse("bug_add"), self.invalid_bad_complexity)
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertIn("complexity_level", form.errors)

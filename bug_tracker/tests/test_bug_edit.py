from django.test import TestCase
from django.urls import reverse
from bug_tracker.models import Bug
from accounts.tests.user_factory import create_user
from bug_tracker.tests.bug_factory import open_bug_data


class BugEditTests(TestCase):
    def setUp(self):
        self.user = create_user()
        bug_data = open_bug_data(self.user)
        bug_data["user_assigned_to"] = (
            self.user
        )  # use actual user instance rather than user id
        self.bug_data = bug_data
        self.bug = Bug.objects.create(**self.bug_data)
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

        self.client.login(username="devuser", password="DevPass123!")

    def test_edit_view_url_exists(self):
        response = self.client.get(reverse("bug_edit", kwargs={"pk": self.bug.pk}))
        self.assertEqual(response.status_code, 200)

    def test_edit_view_contains_bug_title(self):
        response = self.client.get(reverse("bug_edit", kwargs={"pk": self.bug.pk}))
        self.assertContains(response, "Sample Open Bug")

    def test_edit_post_valid_redirects_to_dashboard(self):
        response = self.client.post(
            reverse("bug_edit", kwargs={"pk": self.bug.pk}), self.update_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("dashboard"))

    def test_edit_post_valid_updates_title(self):
        self.client.post(
            reverse("bug_edit", kwargs={"pk": self.bug.pk}), self.update_data
        )
        self.bug.refresh_from_db()
        self.assertEqual(self.bug.bug_title, "Updated Bug")

    def test_edit_post_valid_updates_status(self):
        self.client.post(
            reverse("bug_edit", kwargs={"pk": self.bug.pk}), self.update_data
        )
        self.bug.refresh_from_db()
        self.assertEqual(self.bug.completion_status, "Fixed")

    def test_edit_post_invalid_returns_200_status(self):
        invalid_data = self.update_data.copy()
        invalid_data["complexity_level"] = -5
        response = self.client.post(
            reverse("bug_edit", kwargs={"pk": self.bug.pk}), invalid_data
        )
        self.assertEqual(response.status_code, 200)

    def test_edit_post_invalid_has_form_errors(self):
        invalid_data = self.update_data.copy()
        invalid_data["complexity_level"] = -5
        response = self.client.post(
            reverse("bug_edit", kwargs={"pk": self.bug.pk}), invalid_data
        )
        form = response.context["form"]
        self.assertIn("complexity_level", form.errors)

    def test_edit_post_invalid_uses_form_template(self):
        invalid_data = self.update_data.copy()
        invalid_data["complexity_level"] = -5
        response = self.client.post(
            reverse("bug_edit", kwargs={"pk": self.bug.pk}), invalid_data
        )
        self.assertTemplateUsed(response, "bugs/bug_form.html")

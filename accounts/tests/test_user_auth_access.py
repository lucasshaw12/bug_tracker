from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from bug_tracker.models import Bug
from accounts.tests.user_factory import create_user


class AuthRequiredTests(TestCase):
    def setUp(self):
        self.user = create_user()

        self.bug = Bug.objects.create(
            bug_title="Test Bug",
            bug_description="Test description",
            application_name="TestApp",
            expected_behaviour="Expected",
            actual_behaviour="Actual",
            user_assigned_to=self.user,
            completion_status="Not started",
            complexity_level=1,
            severity_level=1,
        )

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard"))
        self.assertRedirects(response, "/accounts/login/?next=/")

    def test_bug_add_requires_login(self):
        response = self.client.get(reverse("bug_add"))
        self.assertRedirects(response, "/accounts/login/?next=/bug/add/")

    def test_bug_edit_requires_login(self):
        response = self.client.get(reverse("bug_edit", kwargs={"pk": self.bug.pk}))
        self.assertRedirects(
            response, f"/accounts/login/?next=/bug/{self.bug.pk}/edit/"
        )

    def test_bug_delete_requires_login(self):
        response = self.client.get(reverse("bug_delete", kwargs={"pk": self.bug.pk}))
        self.assertRedirects(
            response, f"/accounts/login/?next=/bug/{self.bug.pk}/delete/"
        )

    def test_bug_delete_requires_login(self):
        response = self.client.get(reverse("bug_close", kwargs={"pk": self.bug.pk}))
        self.assertRedirects(
            response, f"/accounts/login/?next=/bug/{self.bug.pk}/close/"
        )

    def test_bug_delete_requires_login(self):
        response = self.client.get(reverse("bug_complete", kwargs={"pk": self.bug.pk}))
        self.assertRedirects(
            response, f"/accounts/login/?next=/bug/{self.bug.pk}/complete/"
        )

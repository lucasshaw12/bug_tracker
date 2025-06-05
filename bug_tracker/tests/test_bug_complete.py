from functools import partial
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from bug_tracker.models import Bug
from accounts.tests.user_factory import create_user


class BugActionTests(TestCase):
    def setUp(self):
        self.user = create_user()
        self.bug_data = {
            "bug_title": "Test Bug",
            "bug_description": "A sample bug",
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

        self.client.login(username="devuser", password="DevPass123!")

    def complete(self):
        return self.client.post(reverse("bug_complete", kwargs={"pk": self.bug.pk}))

    def close(self):
        return self.client.post(reverse("bug_close", kwargs={"pk": self.bug.pk}))

    def test_complete_bug_redirects(self):
        response = self.complete()
        self.assertRedirects(response, reverse("dashboard"))

    def test_complete_bug_sets_status_to_fixed(self):
        self.complete()
        self.bug.refresh_from_db()
        self.assertEqual(self.bug.completion_status, "Fixed")

    def test_complete_bug_updates_completed_on(self):
        original = self.bug.completed_on
        self.complete()
        self.bug.refresh_from_db()
        self.assertGreater(self.bug.completed_on, original)

    def test_close_bug_redirects(self):
        response = self.close()
        self.assertRedirects(response, reverse("dashboard"))

    def test_close_bug_sets_status_to_closed(self):
        self.close()
        self.bug.refresh_from_db()
        self.assertEqual(self.bug.completion_status, "Closed without fix")

    def test_close_bug_updates_completed_on(self):
        original = self.bug.completed_on
        self.close()
        self.bug.refresh_from_db()
        self.assertGreater(self.bug.completed_on, original)

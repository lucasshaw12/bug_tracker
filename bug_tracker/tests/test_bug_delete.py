from django.test import TestCase
from django.urls import reverse
from bug_tracker.models import Bug
from accounts.tests.user_factory import create_user
from bug_tracker.tests.bug_factory import open_bug_data


class BugDeleteTests(TestCase):
    def setUp(self):
        self.user = create_user()
        bug_data = open_bug_data(self.user)
        bug_data["user_assigned_to"] = self.user  # pass actual instance instead of id
        self.bug = Bug.objects.create(**bug_data)
        self.client.login(username="devuser", password="DevPass123!")

    def test_delete_bug_redirects_to_dashboard(self):
        response = self.client.post(reverse("bug_delete", kwargs={"pk": self.bug.pk}))
        self.assertRedirects(response, reverse("dashboard"))

    def test_bug_is_deleted_from_database(self):
        self.client.post(reverse("bug_delete", kwargs={"pk": self.bug.pk}))
        exists = Bug.objects.filter(pk=self.bug.pk).exists()
        self.assertFalse(exists)

    def test_delete_view_requires_login(self):
        self.client.logout()
        response = self.client.post(reverse("bug_delete", kwargs={"pk": self.bug.pk}))
        login_url = reverse("login")
        expected_redirect = (
            f"{login_url}?next={reverse('bug_delete', kwargs={'pk': self.bug.pk})}"
        )
        self.assertRedirects(response, expected_redirect)

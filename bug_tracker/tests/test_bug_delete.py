from django.test import TestCase
from django.urls import reverse
from bug_tracker.models import Bug
from accounts.tests.user_factory import create_user, create_superuser
from bug_tracker.tests.bug_factory import open_bug_data


class BugDeleteTests(TestCase):
    def setUp(self):
        self.user = create_user()
        self.superuser = create_superuser()

        bug_data = open_bug_data(self.user)
        bug_data["user_assigned_to"] = self.user
        self.bug = Bug.objects.create(**bug_data)

    def test_delete_bug_redirects_to_dashboard_for_superuser(self):
        self.client.login(username="adminuser", password="AdminPass123!")
        response = self.client.post(reverse("bug_delete", kwargs={"pk": self.bug.pk}))
        self.assertRedirects(response, reverse("dashboard"))

    def test_bug_is_deleted_from_database_by_superuser(self):
        self.client.login(username="adminuser", password="AdminPass123!")
        self.client.post(reverse("bug_delete", kwargs={"pk": self.bug.pk}))
        exists = Bug.objects.filter(pk=self.bug.pk).exists()
        self.assertFalse(exists)

    def test_delete_view_requires_login(self):
        response = self.client.post(reverse("bug_delete", kwargs={"pk": self.bug.pk}))
        login_url = reverse("login")
        expected_redirect = (
            f"{login_url}?next={reverse('bug_delete', kwargs={'pk': self.bug.pk})}"
        )
        self.assertRedirects(response, expected_redirect)

    def test_non_superuser_cannot_access_delete_view(self):
        self.client.login(username="devuser", password="DevPass123!")
        response = self.client.post(reverse("bug_delete", kwargs={"pk": self.bug.pk}))
        login_url = reverse("login")
        expected_redirect = (
            f"{login_url}?next={reverse('bug_delete', kwargs={'pk': self.bug.pk})}"
        )
        self.assertRedirects(response, expected_redirect)

    def test_non_superuser_does_not_delete_bug(self):
        self.client.login(username="devuser", password="DevPass123!")
        self.client.post(reverse("bug_delete", kwargs={"pk": self.bug.pk}))
        self.assertTrue(Bug.objects.filter(pk=self.bug.pk).exists())

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from bug_tracker.models import Bug
from accounts.tests.user_factory import create_user


class DashboardPageTests(TestCase):
    def setUp(self):
        self.user = create_user()

    def test_root_url_returns_200(self):
        self.client.login(username="devuser", password="DevPass123!")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_dashboard_named_url_returns_200(self):
        self.client.login(username="devuser", password="DevPass123!")
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_uses_dashboard_template(self):
        self.client.login(username="devuser", password="DevPass123!")
        response = self.client.get(reverse("dashboard"))
        self.assertTemplateUsed(response, "dashboard.html")

    def test_dashboard_redirects_if_not_logged_in(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_redirect_url_if_not_logged_in(self):
        response = self.client.get(reverse("dashboard"))
        expected_url = f"{reverse('login')}?next={reverse('dashboard')}"
        self.assertRedirects(response, expected_url)

    def test_dashboard_contains_create_bug_link(self):
        self.client.login(username="devuser", password="DevPass123!")
        response = self.client.get(reverse("dashboard"))
        self.assertContains(response, reverse("bug_add"))

    def test_dashboard_displays_no_bugs_message(self):
        self.client.login(username="devuser", password="DevPass123!")
        response = self.client.get(reverse("dashboard"))
        self.assertContains(response, "No bugs to display.")

    def test_dashboard_displays_created_bug(self):
        Bug.objects.create(
            bug_title="Sample Bug",
            bug_description="A test bug",
            application_name="TestApp",
            expected_behaviour="Should work",
            actual_behaviour="Doesn't work",
            user_assigned_to=self.user,
            completion_status="Not started",
            complexity_level=1,
            severity_level=1,
        )
        self.client.login(username="devuser", password="DevPass123!")
        response = self.client.get(reverse("dashboard"))
        self.assertContains(response, "Sample Bug")

    def test_edit_link_removed_for_non_open_bug(self):
        Bug.objects.create(
            bug_title="Sample Bug",
            bug_description="A test bug",
            application_name="TestApp",
            expected_behaviour="Should work",
            actual_behaviour="Doesn't work",
            user_assigned_to=self.user,
            completion_status="Fixed",
            complexity_level=1,
            severity_level=1,
        )
        self.client.login(username="devuser", password="DevPass123!")
        response = self.client.get(reverse("dashboard"))
        self.assertNotContains(response, 'class="btn btn-link ms-2">Edit</a>')

    def test_edit_link_present_for_open_bug(self):
        Bug.objects.create(
            bug_title="Sample Bug",
            bug_description="A test bug",
            application_name="TestApp",
            expected_behaviour="Should work",
            actual_behaviour="Doesn't work",
            user_assigned_to=self.user,
            completion_status="Not started",
            complexity_level=1,
            severity_level=1,
        )
        self.client.login(username="devuser", password="DevPass123!")
        response = self.client.get(reverse("dashboard"))
        self.assertContains(response, 'class="btn btn-link ms-2">Edit</a>')

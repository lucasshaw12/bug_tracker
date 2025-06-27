from django.test import TestCase
from django.urls import reverse
from bug_tracker.models import Bug
from accounts.tests.user_factory import create_user
from bug_tracker.tests.bug_factory import open_bug_data


class BugCreateTests(TestCase):
    def setUp(self):
        self.user = create_user()
        self.client.login(username="devuser", password="DevPass123!")
        self.valid_data = open_bug_data(self.user)

    def test_get_create_view_returns_bug_form(self):
        response = self.client.get(reverse("bug_add"))
        self.assertEqual(response.status_code, 200)

    def test_post_with_valid_data_redirects(self):
        response = self.client.post(reverse("bug_add"), self.valid_data)
        self.assertEqual(response.status_code, 302)

    def test_post_with_valid_data_creates_bug(self):
        self.client.post(reverse("bug_add"), self.valid_data)
        self.assertEqual(Bug.objects.count(), 1)

    def test_created_bug_has_correct_title(self):
        self.client.post(reverse("bug_add"), self.valid_data)
        bug = Bug.objects.first()
        self.assertEqual(bug.bug_title, "Sample Open Bug")

    def test_created_bug_has_correct_status(self):
        self.client.post(reverse("bug_add"), self.valid_data)
        bug = Bug.objects.first()
        self.assertEqual(bug.completion_status, "Not started")

    def test_post_missing_title_returns_200(self):
        data = self.valid_data.copy()
        data.pop("bug_title")
        response = self.client.post(reverse("bug_add"), data)
        self.assertEqual(response.status_code, 200)

    def test_post_missing_title_has_form_error(self):
        data = self.valid_data.copy()
        data.pop("bug_title")
        response = self.client.post(reverse("bug_add"), data)
        form = response.context["form"]
        self.assertIn("bug_title", form.errors)

    def test_post_invalid_status_returns_bug_add_url(self):
        data = self.valid_data.copy()
        data["completion_status"] = "Invalid Status"
        response = self.client.post(reverse("bug_add"), data)
        self.assertEqual(response.status_code, 200)

    def test_post_invalid_status_has_form_error(self):
        data = self.valid_data.copy()
        data["completion_status"] = "Invalid Status"
        response = self.client.post(reverse("bug_add"), data)
        form = response.context["form"]
        self.assertIn("completion_status", form.errors)
        self.assertTemplateUsed(response, "bugs/bug_form.html")

    def test_post_invalid_complexity_returns_bug_form(self):
        data = self.valid_data.copy()
        data["complexity_level"] = -1
        response = self.client.post(reverse("bug_add"), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bugs/bug_form.html")

    def test_post_invalid_complexity_has_form_error(self):
        data = self.valid_data.copy()
        data["complexity_level"] = -1
        response = self.client.post(reverse("bug_add"), data)
        form = response.context["form"]
        self.assertIn("complexity_level", form.errors)
        self.assertTemplateUsed(response, "bugs/bug_form.html")

    def test_successful_create_redirects_to_dashboard(self):
        response = self.client.post(reverse("bug_add"), self.valid_data)
        self.assertRedirects(response, reverse("dashboard"))

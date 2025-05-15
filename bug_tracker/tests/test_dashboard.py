from django.test import TestCase
from django.urls import reverse


class DashboardPageTests(TestCase):
    def test_url_exists(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_using_name(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_dashboard_page_view(self):
        response = self.client.get(reverse("dashboard"))
        self.assertTemplateUsed(response, "dashboard.html")

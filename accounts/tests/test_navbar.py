from django.test import TestCase
from django.urls import reverse
from accounts.tests.user_factory import create_user, create_superuser


class NavbarTests(TestCase):
    def setUp(self):
        self.user = create_user()

    def test_user_index_link_redirects_to_login_for_non_superuser(self):
        logged_in = self.client.login(username="devuser", password="DevPass123!")
        response = self.client.get(reverse("user_index"))
        self.assertRedirects(
            response, f"{reverse('login')}?next={reverse('user_index')}"
        )

    def test_user_index_link_visible_to_superuser(self):
        self.super_user = create_superuser()
        self.client.login(username="adminuser", password="AdminPass123!")
        response = self.client.get(reverse("dashboard"))
        self.assertContains(response, reverse("user_index"))
        self.assertContains(response, "Users")

    def test_navbar_dropdown_visible_for_logged_in_user(self):
        logged_in = self.client.login(username="devuser", password="DevPass123!")
        self.assertTrue(logged_in, "Login failed for devuser")

        response = self.client.get(reverse("dashboard"))
        self.assertContains(response, self.user.username)
        self.assertContains(response, "Log Out")

from django.test import TestCase
from django.urls import reverse
from accounts.tests.user_factory import create_user


class UserIndexTests(TestCase):
    def setUp(self):
        self.user1 = create_user(
            username="user1",
            email="user1@example.com",
            password="TestPass123!",
            first_name="Alice",
            last_name="Smith",
        )
        self.user2 = create_user(
            username="user2",
            email="user2@example.com",
            password="TestPass123!",
            first_name="Bob",
            last_name="Brown",
        )
        self.client.login(username="user1", password="TestPass123!")

    def test_user_index_template_used(self):
        response = self.client.get(reverse("user_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_index.html")

    def test_user_index_lists_users(self):
        response = self.client.get(reverse("user_index"))
        self.assertContains(response, self.user1.username)
        self.assertContains(response, self.user2.username)

    def test_user_index_displays_all_fields(self):
        response = self.client.get(reverse("user_index"))
        for user in [self.user1, self.user2]:
            self.assertContains(response, user.email)
            self.assertContains(response, user.first_name)
            self.assertContains(response, user.last_name)
            self.assertContains(response, str(user.is_staff))
            self.assertContains(response, str(user.is_active))
            self.assertContains(response, user.date_joined.strftime("%Y"))

    def test_user_index_redirects_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse("user_index"))
        self.assertRedirects(
            response, f"{reverse('login')}?next={reverse('user_index')}"
        )

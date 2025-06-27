from django.test import TestCase
from django.urls import reverse
from accounts.tests.user_factory import create_user, create_superuser

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
        self.admin = create_superuser(
            username="adminuser",
            email="admin@example.com",
            password="AdminPass123!",
            first_name="Admin",
            last_name="User",
        )

    def test_non_superuser_redirected(self):
        self.client.login(username="user1", password="TestPass123!")
        response = self.client.get(reverse("user_index"))
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('user_index')}"
        )

    def test_superuser_sees_index(self):
        self.client.login(username="adminuser", password="AdminPass123!")
        response = self.client.get(reverse("user_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_index.html")

    def test_superuser_lists_usernames(self):
        create_user(username="other", email="o@e.com", password="OtherPass1!")
        self.client.login(username="adminuser", password="AdminPass123!")
        response = self.client.get(reverse("user_index"))
        self.assertContains(response, self.user1.username)

    def test_superuser_displays_all_fields(self):
        self.client.login(username="adminuser", password="AdminPass123!")
        response = self.client.get(reverse("user_index"))
        for user in [self.user1, self.user2]:
            self.assertContains(response, user.email)
            self.assertContains(response, user.first_name)
            self.assertContains(response, user.last_name)
            self.assertContains(response, str(user.is_staff))
            self.assertContains(response, str(user.is_active))

from django.test import TestCase
from django.urls import reverse
from accounts.tests.user_factory import create_user, create_superuser


class UserIndexTests(TestCase):
    def setUp(self):
        self.superuser = create_superuser()
        self.user1 = create_user()

    def test_user_index_redirects_if_not_logged_in(self):
        response = self.client.get(reverse("user_index"))
        self.assertRedirects(
            response, f"{reverse('login')}?next={reverse('user_index')}"
        )

    def test_user_index_redirects_if_not_superuser(self):
        self.client.login(username="devuser", password="DevPass123!")
        response = self.client.get(reverse("user_index"))
        self.assertRedirects(
            response, f"{reverse('login')}?next={reverse('user_index')}"
        )

    def test_user_index_template_used_for_superuser(self):
        self.client.login(username="adminuser", password="AdminPass123!")
        response = self.client.get(reverse("user_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_index.html")

    def test_user_index_lists_users_for_superuser(self):
        self.client.login(username="adminuser", password="AdminPass123!")
        response = self.client.get(reverse("user_index"))
        self.assertContains(response, "devuser")
        self.assertContains(response, "adminuser")

    def test_user_index_displays_all_fields_for_superuser(self):
        self.client.login(username="adminuser", password="AdminPass123!")
        response = self.client.get(reverse("user_index"))
        for user in [self.user1, self.superuser]:
            self.assertContains(response, user.email)
            self.assertContains(response, user.first_name)
            self.assertContains(response, user.last_name)
            self.assertContains(response, str(user.is_staff))
            self.assertContains(response, str(user.is_active))
            self.assertContains(response, user.date_joined.strftime("%Y"))

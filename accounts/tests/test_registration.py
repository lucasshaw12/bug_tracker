from django.test import TestCase
from accounts.models import CustomUser
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignupPageTests(TestCase):
    def test_url_exists(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuseremail@email.com",
                "password1": "StrongPassword123!",
                "password2": "StrongPassword123!",
                "user_role": "Developer",
                "team_name": "QA",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)

        user = get_user_model().objects.first()
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuseremail@email.com")

    def test_signup_form_invalid(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuseremail@email.com",
                "password1": "password1test",
                "password2": "wrongconfirmation",
            },
        )

        form = response.context.get("form")
        self.assertTrue(form.errors)
        self.assertIn("password2", form.errors)

    def test_login_after_signup(self):
        signup_data = {
            "username": "testuser",
            "email": "testuseremail@email.com",
            "password1": "StrongPassword123!",
            "password2": "StrongPassword123!",
            "user_role": "Developer",
            "team_name": "QA",
        }

        self.client.post(reverse("signup"), signup_data)

        login_successful = self.client.login(
            username="testuser", password="StrongPassword123!"
        )

        self.assertTrue(login_successful)

    def test_unsuccessful_login(self):
        get_user_model().objects.create_user(
            username="testuser",
            email="testuseremail@email.com",
            password="CorrectPassword123!",
        )

        login_successful = self.client.login(
            username="testuser", password="WrongPassword!"
        )

        self.assertFalse(login_successful)

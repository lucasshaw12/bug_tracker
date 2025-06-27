from django.test import TestCase
from django.urls import reverse

class SignupRequiredFieldTests(TestCase):
    def setUp(self):
        response = self.client.post(reverse('signup'), {})
        self.form = response.context['form']

    def test_username_required(self):
        self.assertEqual(self.form.errors['username'], ['This field is required.'])

    def test_password1_required(self):
        self.assertEqual(self.form.errors['password1'], ['This field is required.'])

    def test_password2_required(self):
        self.assertEqual(self.form.errors['password2'], ['This field is required.'])

class SignupErrorTests(TestCase):
    def test_empty_signup_shows_required_field_errors(self):
        response = self.client.post(reverse('signup'), data={})
        self.assertEqual(response.status_code, 200)

        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('username', form.errors)
        self.assertIn('password1', form.errors)
        self.assertIn('password2', form.errors)

        content = response.content.decode()
        self.assertIn('class="text-danger small"', content)
        self.assertIn('This field is required.', content)

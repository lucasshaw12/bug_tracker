from django.test import TestCase
from django.urls import reverse

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

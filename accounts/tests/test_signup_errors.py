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


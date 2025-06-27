from django.test import TestCase
from django.urls import reverse

class LoginErrorTests(TestCase):
    def test_empty_form_shows_required_errors(self):
        url = reverse('login')
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            '<div class="text-danger small">This field is required.</div>',
            count=2
        )

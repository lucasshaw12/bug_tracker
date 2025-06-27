from django.test import TestCase
from bug_tracker.forms import BugForm

class BugFormErrorTests(TestCase):
    def test_bug_title_required(self):
        form = BugForm(data={})
        self.assertIn('bug_title', form.errors)
        self.assertEqual(form.errors['bug_title'], ['This field is required.'])

    def test_bug_description_required(self):
        form = BugForm(data={})
        self.assertIn('bug_description', form.errors)
        self.assertEqual(form.errors['bug_description'], ['This field is required.'])

    def test_application_name_required(self):
        form = BugForm(data={})
        self.assertIn('application_name', form.errors)
        self.assertEqual(form.errors['application_name'], ['This field is required.'])

    def test_expected_behaviour_required(self):
        form = BugForm(data={})
        self.assertIn('expected_behaviour', form.errors)
        self.assertEqual(form.errors['expected_behaviour'], ['This field is required.'])

    def test_actual_behaviour_required(self):
        form = BugForm(data={})
        self.assertIn('actual_behaviour', form.errors)
        self.assertEqual(form.errors['actual_behaviour'], ['This field is required.'])

    def test_completion_status_required(self):
        form = BugForm(data={})
        self.assertIn('completion_status', form.errors)
        self.assertEqual(form.errors['completion_status'], ['This field is required.'])

    def test_complexity_level_required(self):
        form = BugForm(data={})
        self.assertIn('complexity_level', form.errors)
        self.assertEqual(form.errors['complexity_level'], ['This field is required.'])

    def test_severity_level_required(self):
        form = BugForm(data={})
        self.assertIn('severity_level', form.errors)
        self.assertEqual(form.errors['severity_level'], ['This field is required.'])

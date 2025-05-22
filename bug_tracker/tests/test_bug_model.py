from django.test import TestCase
from django.urls import reverse

from bug_tracker.models import Bug


class SimpleBugModelTests(TestCase):
    def setUp(self):
        self.bug = Bug.objects.create(
            bug_title="My Bug",
            bug_description="Desc",
            application_name="App",
            expected_behaviour="This",
            actual_behaviour="that",
            completion_status="Not started",
            complexity_level=1,
            severity_level=1,
        )

    def test_str_returns_title(self):
        self.assertEqual(str(self.bug), "My Bug")

    def test_status_class_fixed(self):
        self.bug.completion_status = "Fixed"
        self.bug.save()
        self.assertEqual(self.bug.status_class(), "bg-success text-white")

    def test_status_class_closed_without_fix(self):
        self.bug.completion_status = "Closed without fix"
        self.bug.save()
        self.assertEqual(self.bug.status_class(), "bg-secondary text-white")

    def test_is_complete_status_class_for_fixed(self):
        self.bug.completion_status = "Fixed"
        self.bug.save()
        self.assertEqual(
            self.bug.is_complete_status_class(), "text-white btn-outline-light"
        )

    def test_is_closed_true_for_fixed(self):
        self.bug.completion_status = "Fixed"
        self.bug.save()
        self.assertTrue(self.bug.is_closed())

    def test_is_closed_true_for_closed_without_fix(self):
        self.bug.completion_status = "Closed without fix"
        self.bug.save()
        self.assertTrue(self.bug.is_closed())

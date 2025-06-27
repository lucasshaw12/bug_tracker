from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from bug_tracker.models import Bug
from datetime import timedelta
from django.utils import timezone
from accounts.tests.user_factory import create_user


class BugListViewOrderingTests(TestCase):
    def setUp(self):
        self.user = create_user()
        self.client.login(username="devuser", password="DevPass123!")

        self.bug1 = Bug.objects.create(
            bug_title="Bug 1",
            bug_description="First",
            application_name="App",
            expected_behaviour="Expected",
            actual_behaviour="Actual",
            user_assigned_to=self.user,
            completion_status="Not started",
            complexity_level=1,
            severity_level=1,
            date_raised=timezone.now() - timedelta(days=2),
        )
        self.bug2 = Bug.objects.create(
            bug_title="Bug 2",
            bug_description="Second",
            application_name="App",
            expected_behaviour="Expected",
            actual_behaviour="Actual",
            user_assigned_to=self.user,
            completion_status="Not started",
            complexity_level=1,
            severity_level=1,
            date_raised=timezone.now() - timedelta(days=1),
        )
        self.bug3 = Bug.objects.create(
            bug_title="Bug 3",
            bug_description="Third",
            application_name="App",
            expected_behaviour="Expected",
            actual_behaviour="Actual",
            user_assigned_to=self.user,
            completion_status="Not started",
            complexity_level=1,
            severity_level=1,
            date_raised=timezone.now(),
        )

    def test_bug_list_ordered_by_date_raised(self):
        response = self.client.get(reverse("dashboard"))
        bugs = list(response.context["bug_list"])
        self.assertEqual(bugs, [self.bug1, self.bug2, self.bug3])

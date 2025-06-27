from django.db import models
from django.contrib.auth.models import AbstractUser


# Inheriting from AbstractUser and including extra User model fields.
class CustomUser(AbstractUser):
    user_role = models.CharField(max_length=50, blank=True)
    team_name = models.CharField(max_length=50, blank=True)
    num_bugs_assigned = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

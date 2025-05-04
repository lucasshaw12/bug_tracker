from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


# Custom user form guides
# https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms
# The Custom classes use the default User fields including the ones specified below.
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields = (
            "user_role",
            "team_name",
            "num_bugs_assigned",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields = (
            "user_role",
            "team_name",
            "num_bugs_assigned",
        )

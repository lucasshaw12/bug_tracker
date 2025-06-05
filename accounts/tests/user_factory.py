from django.contrib.auth import get_user_model


def create_user(
    username="devuser",
    email="dev@example.com",
    password="DevPass123!",
    first_name="",
    last_name="",
):
    User = get_user_model()
    return User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )


def create_superuser(
    username="adminuser",
    email="admin@example.com",
    password="AdminPass123!",
    first_name="Admin",
    last_name="User",
):
    User = get_user_model()
    return User.objects.create_superuser(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )

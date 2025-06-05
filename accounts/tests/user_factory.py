from django.contrib.auth import get_user_model


def create_user(username="devuser", email="dev@example.com", password="DevPass123!"):
    User = get_user_model()
    return User.objects.create_user(username=username, email=email, password=password)

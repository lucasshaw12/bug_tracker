from django.urls import path, include
from .views import SignUpView, UserIndexView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("users/", UserIndexView.as_view(), name="user_index"),
]

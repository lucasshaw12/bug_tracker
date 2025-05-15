from django.urls import path
from .views import BugListView, BugUpdateView, BugCreateView

urlpatterns = [
    path("", BugListView.as_view(), name="dashboard"),
    path("bug/add/", BugCreateView.as_view(), name="bug_add"),
    path("bug/<int:pk>/edit/", BugUpdateView.as_view(), name="bug_edit"),
]

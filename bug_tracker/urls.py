from django.urls import path
from .views import (
    BugListView,
    BugCreateView,
    BugUpdateView,
    BugDeleteView,
    BugCompleteView,
    BugCloseView,
)

urlpatterns = [
    path("", BugListView.as_view(), name="dashboard"),
    path("bug/add/", BugCreateView.as_view(), name="bug_add"),
    path("bug/<int:pk>/edit/", BugUpdateView.as_view(), name="bug_edit"),
    path("bug/<int:pk>/complete/", BugCompleteView.as_view(), name="bug_complete"),
    path("bug/<int:pk>/close/", BugCloseView.as_view(), name="bug_close"),
    path("bug/<int:pk>/delete/", BugDeleteView.as_view(), name="bug_delete"),
]

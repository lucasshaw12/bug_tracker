from django.urls import path
from .views import BugTrackerListView

urlpatterns = [path("", BugTrackerListView.as_view(), name="home")]

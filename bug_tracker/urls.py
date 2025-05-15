from django.urls import path
from .views import BugListView

urlpatterns = [path("", BugListView.as_view(), name="dashboard")]

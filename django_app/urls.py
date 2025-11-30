from django.urls import path
from .views import api_info, health, TasksView

urlpatterns = [
    path("api/", api_info, name="api"),
    path("health/", health, name="health"),
    path("tasks/", TasksView.as_view(), name="tasks"),
]


from django.urls import path
from . import views


urlpatterns = [
    path('tasks/', views.TasksListView.as_view()),
    path('createtask/', views.TaskCreateView.as_view()),
]
from django.urls import path
from .views import TaskView,TaskDestroyView
urlpatterns = [
    path('', TaskView.as_view(),name='task'),
    path('<int:pk>/', TaskDestroyView.as_view(), name='task-destroy'),
]
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .serializers import TaskSerializer
from .models import Task


method_decorator(cache_page(60 * 15), name="dispatch")
class TaskView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    
class TaskDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer




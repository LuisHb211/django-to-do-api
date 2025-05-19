from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import Task
from .serializers import TaskSerializer, TaskStatusSerializer

class TaskAPIList(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Task
from .serializers import TaskSerializer, TaskStatusSerializer

class TaskAPIList(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAPIDetail(RetrieveUpdateAPIView):
    queryset =Task.objects.all()
    serializer_class = TaskSerializer
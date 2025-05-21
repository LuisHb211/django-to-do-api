from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer, TaskStatusSerializer

from rest_framework.pagination import PageNumberPagination

# This class was created to change the pagination just for the api
class TaskPagination(PageNumberPagination):
    page_size = 2

class TaskAPIViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
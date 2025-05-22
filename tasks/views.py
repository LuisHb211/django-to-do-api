from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer, TaskStatusSerializer
from rest_framework.pagination import PageNumberPagination
from .permissions import IsOwner
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# This class was created to change the pagination just for the api
class TaskPagination(PageNumberPagination):
    page_size = 2

class TaskAPIViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    # If the user is not logged in, he will just GET/read the objects
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_object(self):
        pk = self.kwargs.get('pk','')
        
        obj = get_object_or_404(
            self.get_object(),
            pk=pk,
        ) 
        self.check_object_permissions(self.request, obj)

        return obj
    
    # Based on IsOwner it will verify if the user is the author and then allow PATCH or DELETE
    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return[IsOwner(),]
        return super().get_permissions()
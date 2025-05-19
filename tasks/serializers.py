from rest_framework import serializers
from .models import TaskStatus, Task

class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ['id', 'title', 'description', 'created_at', 'finish_at', 'status']
	
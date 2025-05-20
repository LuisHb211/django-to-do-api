from rest_framework import serializers
from .models import TaskStatus, Task

class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'finish_at', 'status', 'status_detail']

    status_detail = TaskStatusSerializer(source='status', read_only=True)
    
    # This way I can pass the id of the status at PUT and UPDATE and still saw the name of the status in GET
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['status'] = instance.status.name if instance.status else None
    #     return rep
from django.contrib import admin

from .models import TaskStatus, Task

@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
        
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'created_at', 'finish_at', 'status']
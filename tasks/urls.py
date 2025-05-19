from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
	path('tasks/', 
      views.TaskAPIList().as_view(),
      name='tasks'
    ),
	path('tasks/<int:pk>/',
      views.TaskAPIDetail().as_view(),
      name='task-detail')
	
]

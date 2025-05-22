from django.urls import path, include
from tasks import views
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from .views import TaskAPIViewSet

app_name = 'tasks'

task_api_router = SimpleRouter()
task_api_router.register("tasks/api", TaskAPIViewSet, basename='tasks-api')

urlpatterns = [
    path('tasks/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tasks/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),      

    path('', include(task_api_router.urls))
]



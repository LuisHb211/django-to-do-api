from django.urls import path
from tasks import views
from rest_framework.routers import SimpleRouter

from .views import TaskAPIViewSet

app_name = 'tasks'

router = SimpleRouter()
router.register("tasks", TaskAPIViewSet)

urlpatterns = router.urls
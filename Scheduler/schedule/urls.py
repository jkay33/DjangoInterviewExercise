from rest_framework import routers
from .api import scheduleViewSet

#defining router and urls
#DefaultRouter() includes routes for list, create, retrieve, update, and partial update.
#DefaultRouter() also includes extra route for .json style formats.
router = routers.DefaultRouter()
router.register('api/schedule', scheduleViewSet, 'schedule')
urlpatterns=router.urls

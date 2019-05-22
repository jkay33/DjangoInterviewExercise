from rest_framework import routers
from .api import scheduleViewSet

#defining router and urls
router = routers.DefaultRouter()
router.register('api/schedule', scheduleViewSet, 'schedule')
urlpatterns=router.urls

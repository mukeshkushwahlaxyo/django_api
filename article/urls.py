from django.conf.urls import url, include
from .views import VideoViewSet,UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'vedio', VideoViewSet, basename='MyModel')

urlpatterns = [
    url(r'', include(router.urls)),
    # url(r'video/', VideoViewSet.as_view, name='snippet-list'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_api.views import UserSerializer
from django.conf import settings
from article import router as app2_router
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.extend(app2_router)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'api/', include(('rest_api.urls'),namespace='instance_name')),
    url('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    url(r'^auth/obtain_token/', obtain_jwt_token),
    url(r'^auth/refresh_token/', refresh_jwt_token),  
    # path(r'^api/auth/', include('djoser.urls.authtoken')),
]
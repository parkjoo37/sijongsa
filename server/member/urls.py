from django.conf.urls import include
from rest_framework import routers, serializers, viewsets
from django.urls import path
from member.views import MemberViewSet
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('members', MemberViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('rest-auth/obtain_token/', obtain_jwt_token, name = 'obtain-jwt'),
    path('rest-auth/refresh_token/', refresh_jwt_token, name = 'refresh-jwt'),
    path('rest-auth/verify_token/', verify_jwt_token, name = 'verify-jwt')
]

from django.urls import include, path

from rest_framework import routers

from apps.user.views.owner_view import OwnerViewSet


router = routers.DefaultRouter()
router.register(r'owner', OwnerViewSet, basename='owner')

urlpatterns = [
    path('', include(router.urls)),
]

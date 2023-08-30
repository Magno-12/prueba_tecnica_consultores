from django.urls import include, path

from rest_framework import routers

from apps.property_management.views.predio_view import PredioViewSet


router = routers.DefaultRouter()
router.register(r'predio', PredioViewSet, basename='predio')

urlpatterns = [
    path('', include(router.urls)),
]

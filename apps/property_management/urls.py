from django.urls import include, path

from rest_framework import routers

from apps.property_management.views.predio_view import PredioViewSet
from apps.property_management.views.upload_json_view import UploadJsonView


router = routers.DefaultRouter()
router.register(r'predio', PredioViewSet, basename='predio')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', UploadJsonView.as_view(), name='json-upload'),
]

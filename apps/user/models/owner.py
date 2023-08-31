from django.db import models

from apps.default.models.base_model import BaseModel
from apps.user.utils import TIPO_CHOICES, IDENTIFICACION_CHOICES
from apps.user.models.user import User


class Owner(BaseModel):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    numero_identificacion = models.CharField(max_length=50, unique=True)
    tipo_identificacion = models.CharField(max_length=50, choices=IDENTIFICACION_CHOICES)

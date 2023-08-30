from django.db import models

from apps.default.models.base_model import BaseModel
from apps.user.models.owner import Owner
from apps.property_management.utils import TIPO_CHOICES


class Predio(BaseModel):

    nombre_direccion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    numero_catastral = models.CharField(max_length=30, unique=True)
    numero_matricula = models.CharField(max_length=255, unique=True)
    propietarios = models.ManyToManyField(Owner, related_name="predios")

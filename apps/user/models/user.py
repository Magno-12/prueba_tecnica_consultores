from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)

from apps.default.models.base_model import BaseModel
from apps.user.manager.custom_user_manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(unique=True, db_index=True)
    username = models.CharField(unique=True, max_length=25, db_index=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

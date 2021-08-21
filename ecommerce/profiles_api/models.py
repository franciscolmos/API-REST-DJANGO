from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ MODELO DE BASE DE DATOS PARA LOS USUARIOS DEL SISTEMA"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.TextField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """DEVUELVE EL NOMBRE Y APELLIDO COMPELTO DEL USUARIO"""
        return self.name

    def get_short_name(self):
        """DEVUELVE EL NOMBRE DEL USUARIO"""
        return self.name

    def __str__(self):
        """DEVUELVE UNA REPRENTACION DEL USUARIO EN STRING"""
        return self.email
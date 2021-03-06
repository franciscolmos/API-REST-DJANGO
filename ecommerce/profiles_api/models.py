from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """MANAGER DE PERFILES DE USUARIOS"""

    def get_user_id(self):
        return self.id

    def create_user(self, email, name, password=None):
        """CREAR UN NUEVO USUARIO"""
        if not email:
            raise ValueError('Usuario debe tener un email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """CREAR Y GUARDAR UN SUPER USUARIO CON LOS DATOS ENTRANTES"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ MODELO DE BASE DE DATOS PARA LOS USUARIOS DEL SISTEMA"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.TextField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
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


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text
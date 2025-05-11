from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, nombres, apellido_paterno, apellido_materno, telefono, password=None):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            nombres=nombres,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            telefono=telefono,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombres, apellido_paterno, apellido_materno, telefono, password):
        user = self.create_user(email, nombres, apellido_paterno, apellido_materno, telefono, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombres', 'apellido_paterno', 'apellido_materno', 'telefono']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

from django.db import models
from django.conf import settings

class PerfilCliente(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.usuario.email}'

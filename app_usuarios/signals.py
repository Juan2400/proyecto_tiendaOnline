from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PerfilCliente, CustomUser

@receiver(post_save, sender=CustomUser)
def crear_perfil_cliente(sender, instance, created, **kwargs):
    if created:
        PerfilCliente.objects.create(usuario=instance)

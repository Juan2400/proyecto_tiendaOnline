# models.py en app_producto

from django.db import models

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    foto = models.ImageField(upload_to='productos/', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_producto

    
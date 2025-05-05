from django.contrib import admin
from .models import Categoria, Producto
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria', 'descripcion')  # Muestra estos campos en la lista
    search_fields = ('nombre_categoria',)  # Añade un campo de búsqueda por nombre de la categoría

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'precio', 'categoria', 'activo')  # Muestra estos campos en la lista
    list_filter = ('categoria', 'activo')  # Añade filtros para las categorías y el estado activo
    search_fields = ('nombre_producto',)  # Añade un campo de búsqueda por nombre de producto

# Registrar con la clase personalizada
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)

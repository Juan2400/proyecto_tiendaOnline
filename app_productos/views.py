from django.shortcuts import render
from .models import Producto, Categoria

def productos(request):
    # Obtener todas las categorías
    categorias = Categoria.objects.all()
    
    # Obtener todos los productos activos con sus categorías
    productos = Producto.objects.filter(activo=True).select_related('categoria')
    
    return render(request, 'app_productos/productos.html', {
        'productos': productos,
        'categorias': categorias,
    })
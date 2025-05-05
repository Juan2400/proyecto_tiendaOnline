from django.urls import path
from app_inicio import views #Importamos las vistas de la app_inicio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='Home'),#URL de incio
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
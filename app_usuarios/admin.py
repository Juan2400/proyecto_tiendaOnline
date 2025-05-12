from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, PerfilCliente
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(BaseUserAdmin):
    # Los campos que se mostrarán en el panel de administración
    list_display = ('email', 'nombres', 'apellido_paterno', 'apellido_materno', 'telefono', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Información personal'), {'fields': ('nombres', 'apellido_paterno', 'apellido_materno', 'telefono')}),
        (_('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Fechas importantes'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombres', 'apellido_paterno', 'apellido_materno', 'telefono', 'password1', 'password2'),
        }),
    )

    search_fields = ('email', 'nombres', 'apellido_paterno', 'apellido_materno')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PerfilCliente)

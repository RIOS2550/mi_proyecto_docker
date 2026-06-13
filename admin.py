from django.contrib import admin
from .models import Especie, Propietario, Mascota

@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'telefono', 'email')
    search_fields = ('nombre_completo', 'email')

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'propietario', 'edad', 'fecha_registro')
    list_filter = ('especie',)
    search_fields = ('nombre', 'propietario__nombre_completo')
    ordering = ('-fecha_registro',)
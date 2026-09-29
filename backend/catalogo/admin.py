from django.contrib import admin
from .models import Servicio


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("titulo", "artista", "lanzamiento") # columnas del listado
    search_fields = ("titulo",)
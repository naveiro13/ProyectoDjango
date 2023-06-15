# from django.contrib import admin
# from .models import Producto

# admin.site.register(Producto)

from django.contrib import admin
from .models import Producto

admin.site.site_title = "Productos"
admin.site.site_header = "Nave Automotores"


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("tipo_vehiculo", "marca", "modelo", "anio")  # Campos a mostrar en la lista
    list_filter = ("tipo_vehiculo", "marca")  # Filtros de búsqueda


admin.site.register(Producto, ProductoAdmin)

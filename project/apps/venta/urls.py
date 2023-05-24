from django.urls import path
from . import views

app_name = "venta"

urlpatterns = [
    # Otras URLs de la app "producto" aquí...
    path("", views.mostrar_productos, name="mostrar_productos"),
]

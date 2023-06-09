from django.urls import include, path

# from producto import mostrar_productos
from django.urls import path, include
from . import views
from producto.views import mostrar_productos

app_name = "venta"

urlpatterns = [
    path("productos/", views.mostrar_productos, name="mostrar_ventas"),
    path("mostrar/", views.mostrar_productos, name="mostrar_productos"),
]

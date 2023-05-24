# from django.urls import path

# from . import views

# urlpatterns = [
#   path("", views.index, name="index"),
# ]
from django.urls import path
from . import views

app_name = "producto"

urlpatterns = [
    path("", views.agregar_producto, name="agregar_producto"),
    path("", views.mostrar_productos, name="mostrar_productos"),
]

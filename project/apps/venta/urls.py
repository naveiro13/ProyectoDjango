from django.urls import path
from . import views

app_name = "venta"

urlpatterns = [
    path("", views.mostrar_productos, name="mostrar_productos"),
]

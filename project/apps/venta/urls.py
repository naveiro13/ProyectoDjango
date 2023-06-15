from django.urls import include, path

# from producto import mostrar_productos
from django.urls import path, include
from . import views
from producto.views import mostrar_productos
from django.conf import settings
from django.conf.urls.static import static
from .views import buscar_productos

app_name = "venta"

urlpatterns = [
    path("productos/", views.mostrar_productos, name="mostrar_ventas"),
    path("mostrar/", views.mostrar_productos, name="mostrar_productos"),
    path("buscar/", buscar_productos, name="buscar_productos"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

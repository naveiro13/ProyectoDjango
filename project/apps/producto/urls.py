# from django.urls import path

# from . import views

# urlpatterns = [
#   path("", views.index, name="index"),
# ]
from django.urls import path

# from . import views
from django.urls import path
from producto import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "producto"

urlpatterns = [
    path("agregar/", views.agregar_producto, name="agregar_producto"),
    path("mostrar/", views.mostrar_productos, name="mostrar_productos"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

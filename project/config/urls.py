from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("home.urls", "home"))),
    path("producto/", include(("producto.urls", "producto"))),
    path("venta/", include(("venta.urls", "venta"))),
    path("copyright/", include(("copyright.urls", "copyright"))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

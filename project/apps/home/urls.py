# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views

# urlpatterns = [
#   path("", views.index, name="index"),
#  path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
# ]
# urlpatterns += staticfiles_urlpatterns()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("quienes_somos/", views.quienes_somos, name="quienes_somos"),
    path("login/", auth_views.LoginView.as_view(template_name="home/login.html"), name="login"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

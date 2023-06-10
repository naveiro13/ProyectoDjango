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

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", auth_views.LoginView.as_view(template_name="home/login.html"), name="login"),
]
urlpatterns += staticfiles_urlpatterns()

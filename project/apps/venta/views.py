# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render


# def index(request: HttpRequest) -> HttpResponse:
#   return render(request, "venta/index.html")


from django.shortcuts import render
from producto.models import Producto


def mostrar_productos(request):
    productos = Producto.objects.all()
    return render(request, "venta/index.html", {"productos": productos})

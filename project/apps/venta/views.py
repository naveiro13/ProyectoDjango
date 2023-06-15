# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render


# def index(request: HttpRequest) -> HttpResponse:
#   return render(request, "venta/index.html")


from django.shortcuts import render
from producto.models import Producto
from django.shortcuts import render
from producto.models import Producto
from django.db.models import Q


def mostrar_productos(request):
    productos = Producto.objects.all()
    return render(request, "venta/index.html", {"productos": productos})


def buscar_productos(request):
    term = request.GET.get("q")
    productos = Producto.objects.filter(
        Q(tipo_vehiculo__icontains=term)
        | Q(marca__icontains=term)
        | Q(modelo__icontains=term)
        | Q(anio__icontains=term)
    )
    context = {"productos": productos, "term": term}
    return render(request, "venta/lista_productos.html", context)

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Producto

from django.shortcuts import render
from .models import Producto


def mostrar_productos(request):
    productos = Producto.objects.all()
    return render(request, "producto/mostrar_productos.html", {"productos": productos})


def agregar_producto(request):
    if request.method == "POST":
        tipo_vehiculo = request.POST.get("tipo_vehiculo")
        marca = request.POST.get("marca")
        modelo = request.POST.get("modelo")
        anio = request.POST.get("anio")

        producto = Producto(tipo_vehiculo=tipo_vehiculo, marca=marca, modelo=modelo, anio=anio)
        producto.save()

        return redirect("producto:mostrar_productos")  # Reemplaza "nombre_de_la_app" con el nombre real de tu app

    return render(request, "producto/index.html")


# def index(request: HttpRequest) -> HttpResponse:
# return render(request, "producto/index.html")

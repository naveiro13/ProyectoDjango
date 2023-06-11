from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Producto


@login_required(login_url="home:login")
def agregar_producto(request):
    if request.method == "POST":
        tipo_vehiculo = request.POST.get("tipo_vehiculo")
        marca = request.POST.get("marca")
        modelo = request.POST.get("modelo")
        anio = request.POST.get("anio")
        detalle = request.POST.get("detalle")
        imagen = request.FILES.get("imagen")

        producto = Producto(
            tipo_vehiculo=tipo_vehiculo, marca=marca, modelo=modelo, anio=anio, detalle=detalle, imagen=imagen
        )

        if imagen:
            fs = FileSystemStorage()
            filename = fs.save(imagen.name, imagen)
            producto.imagen = fs.url(filename)

        producto.save()

        return redirect("producto:mostrar_productos")

    return render(request, "producto/index.html")


from django.shortcuts import render
from .models import Producto


def mostrar_productos(request):
    productos = Producto.objects.all()
    return render(request, "producto/mostrar_productos.html", {"productos": productos})


# def index(request: HttpRequest) -> HttpResponse:
# return render(request, "producto/index.html")

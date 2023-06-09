from django.db import models


class Producto(models.Model):
    tipo_vehiculo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    detalle = models.CharField(max_length=100, default="")  # Nuevo campo para el detalle

    imagen = models.ImageField(upload_to="productos/", blank=True, null=True)

    def __str__(self):
        return self.tipo_vehiculo


# imagen = models.ImageField(upload_to="producto_imagenes/")  # Nuevo campo para la imagen
imagen = models.ImageField(upload_to="productos/", blank=True, null=True)

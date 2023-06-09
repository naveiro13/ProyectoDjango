from django.db import models


class Producto(models.Model):
    tipo_vehiculo = models.CharField(max_length=100, unique=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    detalle = models.TextField()  # Nuevo campo para el detalle
    imagen = models.ImageField(upload_to="producto_imagenes/")  # Nuevo campo para la imagen

    def __str__(self):
        return self.tipo_vehiculo

from django.db import models


class Producto(models.Model):
    tipo_vehiculo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()

    def __str__(self):
        return self.tipo_vehiculo

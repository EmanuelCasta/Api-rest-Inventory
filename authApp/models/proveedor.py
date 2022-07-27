from django.db import models

class Proveedor(models.Model):
    idProveedor = models.IntegerField(primary_key=True)
    Descripcion = models.CharField('Descripcion', max_length=250, unique=False)
    NombreProveedor = models.CharField ('Proveedor', max_length=180, unique= True)
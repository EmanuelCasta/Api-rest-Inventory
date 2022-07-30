from django.db import models

class Proveedor(models.Model):
    Proveedor_id = models.IntegerField(primary_key=True)
    Descripcion = models.CharField('Descripcion', max_length=250, unique=False)
    NombreProveedor = models.CharField ('NombreProveedor', max_length=180, unique= True)
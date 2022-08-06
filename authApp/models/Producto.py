from django.db  import models
from .proveedor import Proveedor
from .Categoria  import Categoria
from .Empresa  import Empresa

class Producto(models.Model):
    Producto_id = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre',max_length=500, help_text="Ingresa la el nombre",unique=True)
    fechaIngreso = models.DateTimeField(auto_now_add=True)
    precio = models.FloatField(default=0)
    descripcion = models.CharField('descripcion',max_length=500, help_text="Ingresa la descripcion del producto")
    cantidad= models.IntegerField(default=0)
    Proveedor=   models.ForeignKey(Proveedor, related_name='proveedor', on_delete=models.CASCADE)
    Categoria=   models.ForeignKey(Categoria, related_name='categoria', on_delete=models.CASCADE)
    Empresa=   models.ForeignKey(Empresa, related_name='empresa', on_delete=models.CASCADE)

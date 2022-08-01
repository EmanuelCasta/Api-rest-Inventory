from django.db  import models
from .proveedor import Proveedor
from .Categoria  import Categoria
from .Empresa  import Empresa

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    fechaIngreso = models.DateTimeField(auto_now_add=True)
    precio = models.FloatField(default=0)
    descripcion = models.CharField('Descripcion',max_length=500, help_text="Ingresa la descripcion del producto")
    cantidad= models.IntegerField(default=0)
    idProveedor=   models.ForeignKey(Proveedor, related_name='proveedor', on_delete=models.CASCADE)
    idCategoria=   models.ForeignKey(Categoria, related_name='categoria', on_delete=models.CASCADE)
    idEmpresa=   models.ForeignKey(Empresa, related_name='empresa', on_delete=models.CASCADE)

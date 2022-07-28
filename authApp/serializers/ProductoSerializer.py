from authApp.models.Producto import Producto
from authApp.models.proveedor import Proveedor
from authApp.models.Categoria import Categoria
from rest_framework import serializers
from authApp.serializers.CategoriaSerializer import CategoriaSerializer
from authApp.serializers.ProveedorSerializer import ProveedorSerializer

class ProductoSerializer(serializers.ModelSerializer):
    categoria = Categoria()
    proveedor = Proveedor()

    class Meta:
        model = Producto()
        fields = ["idProducto","fechaIngreso","precio","descripcion","cantidad","idProveedor","idCategoria"]

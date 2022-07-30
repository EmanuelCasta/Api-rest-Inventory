from authApp.models.Producto import Producto
from authApp.models.proveedor import Proveedor
from authApp.models.Categoria import Categoria
from rest_framework import serializers
from authApp.serializers.categoriaSerializer import CategoriaSerializer
from authApp.serializers.proveedorSerializer import ProveedorSerializer

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    proveedor = ProveedorSerializer()
    idProveedor =  serializers.IntegerField(write_only=True)
    idCategoria=  serializers.IntegerField(write_only=True)

    class Meta:
        model = Producto
        ordering = ["-idProducto"]
        fields = ["idProducto","fechaIngreso","precio","descripcion","cantidad","idProveedor","idCategoria"]
        depth = 1
    
    def create(self, validated_data):
        #proveedorInstance = Proveedor.objects.create(**validated_data)
        #categoriarInstance = Categoria.objects.create(**validated_data)
        productoInstance = Producto.objects.create(**validated_data)
        return productoInstance
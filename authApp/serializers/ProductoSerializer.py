from authApp.models.Producto import Producto
from authApp.models.proveedor import Proveedor
from authApp.models.Categoria import Categoria
from rest_framework import serializers
from authApp.serializers.CategoriaSerializer import CategoriaSerializer
from authApp.serializers.ProveedorSerializer import ProveedorSerializer

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    proveedor = ProveedorSerializer()
    idProveedor =  serializers.IntegerField(write_only=True)
    idCategoria=  serializers.IntegerField(write_only=True)

    class Meta:
        model = Producto()
        ordering = ["-idProducto"]
        fields = ["idProducto","fechaIngreso","precio","descripcion","cantidad","idProveedor","idCategoria"]
        depth = 1
    
    def create(self, validated_data):
        proveedorInstance = Proveedor.objects.create(**validated_data)
        categoriarInstance = Categoria.objects.create(**validated_data)
        productoInstance = Producto.objects.create(idProveedor=proveedorInstance,idCategoria=categoriarInstance, **validated_data)
        return productoInstance
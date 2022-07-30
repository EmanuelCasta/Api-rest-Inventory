from authApp.models.Producto import Producto
from authApp.models.proveedor import Proveedor
from authApp.models.Categoria import Categoria
from rest_framework import serializers
from authApp.serializers.categoriaSerializer import CategoriaSerializer
from authApp.serializers.proveedorSerializer import ProveedorSerializer

class ProductoSerializer(serializers.ModelSerializer):
    #categoria = CategoriaSerializer()
    #proveedor = ProveedorSerializer()
    idProveedor_id =  serializers.IntegerField(write_only=True)
    idCategoria_id=  serializers.IntegerField(write_only=True)
    #categoria = CategoriaSerializer(read_only=True)
    #proveedor = ProveedorSerializer(read_only=True)
    #idProveedor = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Proveedor.objects.all(), source='idProveedor')
    #idCategoria = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Categoria.objects.all(), source='idCategoria')

    class Meta:
        model = Producto
        ordering = ["-idProducto"]
        fields = ["idProducto","nombre","precio","descripcion","cantidad","idProveedor_id","idCategoria_id"]
        depth = 1
    
    def create(self, validated_data):
        #proveedorInstance = Proveedor.objects.create(**validated_data)
        #categoriarInstance = Categoria.objects.create(**validated_data)
        productoInstance = Producto.objects.create(**validated_data)
        return productoInstance
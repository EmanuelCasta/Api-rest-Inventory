from authApp.models.Producto import Producto
from authApp.models.proveedor import Proveedor
from authApp.models.Categoria import Categoria
from authApp.models.Empresa import Empresa
from rest_framework import serializers
from authApp.serializers.CategoriaSerializer import CategoriaSerializer
from authApp.serializers.ProveedorSerializer import ProveedorSerializer
from authApp.serializers.EmpresaSerializer import EmpresaSerializer

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    proveedor = ProveedorSerializer()
    idProveedor =  serializers.IntegerField(write_only=True)
    idCategoria=  serializers.IntegerField(write_only=True)
    idEmpresa=  serializers.IntegerField(write_only=True)

    class Meta:
        model = Producto()
        ordering = ["-idProducto"]
        fields = ["idProducto","fechaIngreso","precio","descripcion","cantidad","idProveedor","idCategoria","idEmpresa"]
        depth = 1

    def create(self, validated_data):
        proveedorInstance = Proveedor.objects.create(**validated_data)
        categoriarInstance = Categoria.objects.create(**validated_data)
        EmpresaInstance = Empresa.objects.create(**validated_data)
        productoInstance = Producto.objects.create(idProveedor=proveedorInstance,idCategoria=categoriarInstance,idEmpresa=EmpresaInstance, **validated_data)
        return productoInstance
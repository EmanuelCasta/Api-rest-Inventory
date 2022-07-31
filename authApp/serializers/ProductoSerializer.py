from authApp.models.Producto import Producto
from authApp.models.proveedor import Proveedor
from authApp.models.Categoria import Categoria
from rest_framework import serializers
from authApp.serializers.categoriaSerializer import CategoriaSerializer
from authApp.serializers.proveedorSerializer import ProveedorSerializer

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    proveedor = ProveedorSerializer(read_only=True)
    Proveedor_id =  serializers.IntegerField()
    Categoria_id=  serializers.IntegerField()
    #categoria = CategoriaSerializer(read_only=True)
    #proveedor = ProveedorSerializer(read_only=True)
    #idProveedor = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Proveedor.objects.all(), source='idProveedor')
    #idCategoria = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Categoria.objects.all(), source='idCategoria')

    class Meta:
        model = Producto
        fields = ["Producto_id","nombre","precio","descripcion","cantidad","Proveedor_id","Categoria_id","categoria","proveedor"]
     
    
    def create(self, validated_data):
        #proveedorInstance = Proveedor.objects.create(**validated_data)
        #categoriarInstance = Categoria.objects.create(**validated_data)
        productoInstance = Producto.objects.create(**validated_data)
        return productoInstance
    
    def to_representation(self,obj):
        producto = Producto.objects.get(Producto_id=obj.Producto_id)
        categoria =Categoria.objects.get(Categoria_id=obj.Categoria_id)
        proveedor =Proveedor.objects.get(Proveedor_id=obj.Proveedor_id)
        return {
            'Producto_id':producto.Producto_id,
            "nombre":producto.nombre,
            'precio':producto.precio,
            'fechaIngreso':producto.fechaIngreso,
            'cantidad':producto.cantidad,
            'descripcion':producto.descripcion,
            'categoria':{
                'id':categoria.Categoria_id,
                "nombre":categoria.nombreCategoria,
            },
            'proveedor':{
                'id':proveedor.Proveedor_id,
                "nombre":proveedor.NombreProveedor,
                
            }
        }
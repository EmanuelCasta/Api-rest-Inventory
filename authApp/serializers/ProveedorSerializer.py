from authApp.models.Proveedor import Proveedor
from rest_framework import serializers

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ["Proveedor_id","Descripcion","NombreProveedor"]
from authApp.models.Empresa import Empresa
from rest_framework import serializers

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ["idEmpresa","NombreEmpresa","NIT"]
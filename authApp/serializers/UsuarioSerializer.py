from rest_framework import serializers
from authApp.models.usuario import Usuario
from authApp.models.Empresa import Empresa
from authApp.serializers.EmpresaSerializer import EmpresaSerializer


class UsuarioSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer()
    class Meta:
        model = Usuario
        fields = ['id','Username','password','Name','Email','empresa']

    def create(self, validated_data):
        empresaData = validated_data.pop('empresa')
        userInstance = Usuario.objects.create(**validated_data)
        Empresa.objects.create(**empresaData)
        return userInstance

    def to_representation(self,obj):
        user = Usuario.objects.get(id=obj.id)
        empresa = Empresa.objects.get(Empresa_id=obj.Empresa_id)
        return {
            'id':user.id,
            'username':user.Username,
            'name':user.Name,
            'email':user.Email,
            'empresa':{
                'Empresa_id':empresa.Empresa_id,
                'NombreEmpresa':empresa.NombreEmpresa,
                'NIT':empresa.NIT,
            }
        }
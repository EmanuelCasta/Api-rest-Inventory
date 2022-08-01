from curses.ascii import US
from rest_framework import serializers
from authApp.models.Usuario import Usuario
from authApp.models.Empresa import Empresa
from authApp.serializers.EmpresaSerializer import EmpresaSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer()
    class Meta:
        model = Usuario
        fields = ['idUsuario','Username','Password','Name','Email','empresa']

    def create(self, validated_data):
        empresatData = validated_data.pop('empresa')
        userInstance = Usuario.objects.create(**validated_data)
        Empresa.objects.create(user=userInstance, **empresatData)
        return userInstance

    def to_representation(self,obj):
        user = Usuario.objects.get(id=obj.id)
        empresa = Empresa.objects.get(user=obj.id)
        return {
            'id':user.id,
            'username':user.username,
            'name':user.name,
            'email':user.email,
            'empresa':{
                'id':empresa.id,
                'nombreEmpresa':empresa.NombreEmpresa,
                'NIT':empresa.NIT,
            }
        }
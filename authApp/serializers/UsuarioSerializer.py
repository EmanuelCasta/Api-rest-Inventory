from curses.ascii import US
from rest_framework import serializers
from authApp.models.usuario import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','Username','password','Name','Email','Empresa_id']

    def create(self, validated_data):
        userInstance = Usuario.objects.create(**validated_data)
        return userInstance

    def to_representation(self,obj):
        user = Usuario.objects.get(id=obj.id)
        return {
            'id':user.id,
            'username':user.Username,
            'name':user.Name,
            'email':user.Email,
        }
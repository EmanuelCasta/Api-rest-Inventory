from lib2to3.pgen2 import token
from urllib import request
from rest_framework import status,views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.models.usuario import Usuario
from authApp.serializers.UsuarioSerializer import UsuarioSerializer

class UsuarioCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"Username":request.data["Username"],
                     "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        user = Usuario.objects.filter(Username = request.data["Username"]).first()
        user_serializer = UsuarioSerializer(user)

        return Response({"Security":tokenSerializer.validated_data,"Info_user":user_serializer.data}, status=status.HTTP_201_CREATED)

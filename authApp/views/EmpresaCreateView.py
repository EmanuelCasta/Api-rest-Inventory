from lib2to3.pgen2 import token
from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.EmpresaSerializer import EmpresaSerializer

class EmpresaCreateView(views.APIView):

    def post(self,request,*arg,**kwargs):
        serializer = EmpresaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)
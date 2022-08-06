from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.proveedor import Proveedor
from authApp.serializers.ProveedorSerializer import ProveedorSerializer

class ProveedorDetailView(generics.RetrieveAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

#metodo obtener
    def get(self,request,*args,**kwargs):
        if kwargs['pk'] is not None:
            proveedor = Proveedor.objects.filter(Proveedor_id = kwargs['pk']).first()
           
            proveedor_serializer = ProveedorSerializer(proveedor)
            if proveedor_serializer.data["NombreProveedor"] != "":
                return Response(proveedor_serializer.data,status=status.HTTP_200_OK)
       
        return Response({"Error":"No found"},status=status.HTTP_501_NOT_IMPLEMENTED)

#metodo Actualizar    
    def put(self, request,*args,**kwargs):
        proveedor = Proveedor.objects.filter(Proveedor_id = kwargs['pk']).first()
        proveedor_serializer = self.serializer_class(proveedor,data=request.data)
        if proveedor_serializer.is_valid():
            proveedor_serializer.save()
            return Response(proveedor_serializer.data,status=status.HTTP_200_OK)
        return Response(proveedor_serializer.errors)

#metodo borrar
    def delete(self, request,*args,**kwargs):
        proveedor = Proveedor.objects.filter(Proveedor_id = kwargs['pk']).first()
        proveedor.delete()
        return Response({"status": f"{status.HTTP_200_OK}"},status=status.HTTP_200_OK)


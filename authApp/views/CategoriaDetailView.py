from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.Categoria import Categoria
from authApp.serializers.categoriaSerializer import CategoriaSerializer

class CategoriaDetailView(generics.RetrieveAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

#metodo obtener
    def get(self,request,*args,**kwargs):
        if kwargs['pk'] is not None:
            Categoria = Categoria.objects.filter(Proveedor_id = kwargs['pk']).first()
           
            Categoria_serializer = CategoriaSerializer(Categoria)
            if Categoria_serializer.data["NombreCategoria"] != "":
                return Response(Categoria_serializer.data,status=status.HTTP_200_OK)
       
        return Response({"Error":"No found"},status=status.HTTP_501_NOT_IMPLEMENTED)

#metodo Actualizar    
    def put(self, request,*args,**kwargs):
        Categoria = Categoria.objects.filter(Categoria_id = kwargs['pk']).first()
        Categoria_serializer = self.serializer_class(Categoria,data=request.data)
        if Categoria_serializer.is_valid():
            Categoria_serializer.save()
            return Response(Categoria_serializer.data,status=status.HTTP_200_OK)
        return Response(Categoria_serializer.errors)

#metodo borrar
    def delete(self, request,*args,**kwargs):
        Categoria = Categoria.objects.filter(Categoria_id = kwargs['pk']).first()
        Categoria.delete()
        return Response({"status": f"{status.HTTP_200_OK}"},status=status.HTTP_200_OK)


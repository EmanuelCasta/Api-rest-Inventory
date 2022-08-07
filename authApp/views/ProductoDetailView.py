from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.Producto import Producto
from authApp.serializers.ProductoSerializer import ProductoSerializer

class ProductoDetailView(generics.RetrieveAPIView):
    queryset = Producto.objects.all
    serializer_class = ProductoSerializer

    permission_classes = (IsAuthenticated,)

    def get(self,request,*args,**kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

       
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        
        if kwargs['pkProducto'] is not None:
            producto = Producto.objects.filter(Producto_id = kwargs['pkProducto']).first()
            if producto:
                producto_serializer = ProductoSerializer(producto)
                if producto_serializer.data["nombre"] != "":
                    return Response(producto_serializer.data,status=status.HTTP_200_OK)
        return Response({"Error":"No found"},status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,*args,**kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

       
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        producto = Producto.objects.filter(Producto_id = kwargs['pkProducto']).first()
        producto_serializer = self.serializer_class(producto,data=request.data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data,status=status.HTTP_200_OK)
        return Response(producto_serializer.errors)

    def delete(self, request,*args,**kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

       
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
            
        producto = Producto.objects.filter(Producto_id = kwargs['pkProducto']).first()
        producto.delete()
        return Response({"status": f"{status.HTTP_200_OK}"},status=status.HTTP_200_OK)

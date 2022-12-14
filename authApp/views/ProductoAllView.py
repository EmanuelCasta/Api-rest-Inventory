from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.Producto import Producto
from authApp.serializers.ProductoSerializer import ProductoSerializer

class ProductoAllView(generics.RetrieveAPIView):
    queryset = Producto.objects.all
    serializer_class = ProductoSerializer

    #permisio
    #Cuando se cree el user 
    permission_classes = (IsAuthenticated,)

    def get(self,request,*args,**kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

       
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        #producto = self.get_queryset(kwargs['pk'])
        
        productos = self.queryset()
        if productos:
            producto_serializer=self.serializer_class(productos,many =True)
            
            return Response(producto_serializer.data,status=status.HTTP_200_OK)
        return Response(producto_serializer.data,status=status.HTTP_409_CONFLICT)
        
        
  

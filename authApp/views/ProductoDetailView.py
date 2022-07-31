from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.Producto import Producto
from authApp.serializers.ProductoSerializer import ProductoSerializer

class ProductoDetailView(generics.RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    #permisio
    #Cuando se cree el user 
    #permission_classes = (IsAuthenticated,)


    def get(self,request,*args,**kwargs):
        #token = request.META.get('HTTP_AUTHORIZATION')[7:]
        #tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        #valid_data = tokenBackend.decode(token,verify=False)
        #print(request.__dict__,"===================================================================================")
        #if kwargs['pk'] != request['Producto_id'] :
        #    stringResponse = {'detail':'error Request'}
        #    return Response(stringResponse, status=status.HTTP_404_NOT_FOUND)

        #producto = self.get_queryset(kwargs['pk'])
        if kwargs['pk'] is not None:
            producto = Producto.objects.filter(Producto_id = kwargs['pk']).first()
           
            producto_serializer = ProductoSerializer(producto)
            if producto_serializer.data["nombre"] != "":
                return Response(producto_serializer.data,status=status.HTTP_200_OK)
       
        return Response({"Error":"No found"},status=status.HTTP_501_NOT_IMPLEMENTED)
    
    def put(self, request,*args,**kwargs):
        producto = Producto.objects.filter(Producto_id = kwargs['pk']).first()
        producto_serializer = self.serializer_class(producto,data=request.data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data,status=status.HTTP_200_OK)
        return Response(producto_serializer.errors)

    def delete(self, request,*args,**kwargs):
        producto = Producto.objects.filter(Producto_id = kwargs['pk']).first()
        producto.delete()
        return Response({"status": f"{status.HTTP_200_OK}"},status=status.HTTP_200_OK)

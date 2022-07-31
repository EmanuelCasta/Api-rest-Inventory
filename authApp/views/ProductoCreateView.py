from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.productoSerializer import ProductoSerializer

class ProductoCreateView(views.APIView):

    def post(self,request,*arg,**kwargs):
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #colocar el token de inicios

        return Response(serializer.validated_data,status=status.HTTP_201_CREATED)


    
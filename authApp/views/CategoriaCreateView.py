from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.CategoriaSerializer import CategoriaSerializer

class CategoriaCreateView (views.APIView):
    
    def post(self, request, *args, **kwargs):
        #Proveedor no es autoincrementable
        serializer = CategoriaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.ProveedorSerializer import ProveedorSerializer

class ProveedorCreateView (views.APIView):
    def post(selt, request, *args, **kwargs):
        serializer = ProveedorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
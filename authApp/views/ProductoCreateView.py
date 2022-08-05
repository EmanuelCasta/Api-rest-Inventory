from rest_framework import status, views
from django.conf import settings
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.ProductoSerializer import ProductoSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

class ProductoCreateView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request,*arg,**kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
            
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #colocar el token de inicios

        return Response(serializer.validated_data,status=status.HTTP_201_CREATED)


    
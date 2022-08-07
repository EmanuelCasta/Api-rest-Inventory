from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.Empresa import Empresa
from authApp.serializers.EmpresaSerializer import EmpresaSerializer

class EmpresaDetailView(generics.RetrieveAPIView):
    queryset = Empresa.objects.all
    serializer_class = EmpresaSerializer
   

    def get(self, request, *args, **kwargs):

        empresa = self.queryset()
        if empresa:
            empresa_serializer=self.serializer_class(empresa,many =True)
            return Response(empresa_serializer.data,status=status.HTTP_200_OK)
        return Response(empresa_serializer.data,status=status.HTTP_409_CONFLICT)
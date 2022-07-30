from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.Producto import Producto
from authApp.serializers.productoSerializer import ProductoSerializer

class ProductoDetailView(generics.RetrieveAPIView):
    queryset = Producto.objects.all()
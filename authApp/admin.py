from django.contrib import admin
from authApp.models.Producto import Producto
from authApp.models.Proveedor import Proveedor
from authApp.models.Categoria import Categoria

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Producto)
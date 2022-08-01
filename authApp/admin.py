from django.contrib import admin
from authApp.models.Producto import Producto
from authApp.models.proveedor import Proveedor
from authApp.models.Categoria import Categoria
from authApp.models.usuario import Usuario
from authApp.models.Empresa import Empresa

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Empresa)
from django.contrib import admin
<<<<<<< HEAD
from authApp.models.Producto import Producto
=======
from .models.proveedor import Proveedor

from .models.category import Category

admin.site.register(Proveedor)
admin.site.register(Category)

>>>>>>> d7fe0b24bd405e67f1dade532a06c496a84c34fe
# Register your models here.

admin.site.register(Producto)
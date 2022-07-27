from django.contrib import admin
from .models.proveedor import Proveedor

from .models.category import Category

admin.site.register(Proveedor)
admin.site.register(Category)

# Register your models here.

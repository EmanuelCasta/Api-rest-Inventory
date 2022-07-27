from django.db import models

class Category(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    NombreCategoria = models.CharField ('Categoria', max_length=180, unique= True)
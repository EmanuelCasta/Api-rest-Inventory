from django.db import models

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    NombreCategoria = models.CharField ('Categoria', max_length=180, unique= True)
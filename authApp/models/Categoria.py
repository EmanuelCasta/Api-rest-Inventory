from django.db import models

class Categoria(models.Model):
    Categoria_id = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField ('nombreCategoria', max_length=180, unique= True)
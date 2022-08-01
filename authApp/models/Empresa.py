from django.db import models

class Empresa(models.Model):
    idEmpresa = models.AutoField(primary_key=True)
    NombreEmpresa = models.CharField ('Empresa', max_length=180, unique= True)
    NIT = models.CharField ('NIT', max_length=180, unique= True)
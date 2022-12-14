# Generated by Django 4.0.6 on 2022-07-30 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0002_producto_nombre_alter_producto_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='NombreCategoria',
        ),
        migrations.AddField(
            model_name='categoria',
            name='nombreCategoria',
            field=models.CharField(default=1, max_length=180, unique=True, verbose_name='nombreCategoria'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='NombreProveedor',
            field=models.CharField(max_length=180, unique=True, verbose_name='NombreProveedor'),
        ),
    ]

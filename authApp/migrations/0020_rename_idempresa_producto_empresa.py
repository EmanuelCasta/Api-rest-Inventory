# Generated by Django 4.0.6 on 2022-08-07 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0019_rename_empresa_producto_idempresa_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='idEmpresa',
            new_name='Empresa',
        ),
    ]

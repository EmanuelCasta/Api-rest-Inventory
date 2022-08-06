# Generated by Django 4.0.6 on 2022-07-30 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0005_rename_idcategoria_categoria_categoria_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(help_text='Ingresa la el nombre', max_length=500, unique=True, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=100, unique=True, verbose_name='Email'),
        ),
    ]
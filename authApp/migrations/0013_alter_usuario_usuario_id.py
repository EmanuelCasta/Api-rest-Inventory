# Generated by Django 4.0.6 on 2022-08-01 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0012_rename_empresa_id_usuario_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Usuario_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]

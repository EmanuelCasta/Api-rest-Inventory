# Generated by Django 4.0.6 on 2022-08-01 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0015_alter_usuario_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=256, verbose_name='password'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-06 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webHuertita', '0012_rename_genero_id_usuario_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default='default_username', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='contraseña',
            field=models.CharField(max_length=30),
        ),
    ]

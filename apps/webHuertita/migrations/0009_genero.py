# Generated by Django 4.2.2 on 2023-06-22 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webHuertita', '0008_venta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_genero', models.CharField(max_length=50)),
            ],
        ),
    ]

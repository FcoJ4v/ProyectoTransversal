# Generated by Django 4.2.2 on 2023-07-07 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webHuertita', '0024_rename_categoria_id_venta_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='categoria',
            new_name='categoria_id',
        ),
    ]

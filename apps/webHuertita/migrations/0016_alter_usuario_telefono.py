# Generated by Django 4.2.2 on 2023-07-07 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webHuertita', '0015_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
    ]

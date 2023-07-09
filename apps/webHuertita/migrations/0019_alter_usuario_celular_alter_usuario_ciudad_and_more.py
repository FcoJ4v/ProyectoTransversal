# Generated by Django 4.2.2 on 2023-07-07 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webHuertita', '0018_alter_usuario_celular_alter_usuario_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='celular',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ciudad',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='comuna',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='depto',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='region',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
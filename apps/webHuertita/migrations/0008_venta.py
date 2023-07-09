# Generated by Django 4.2.2 on 2023-06-22 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webHuertita', '0007_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_compra', models.DateField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webHuertita.usuario')),
                ('prod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webHuertita.producto')),
            ],
        ),
    ]

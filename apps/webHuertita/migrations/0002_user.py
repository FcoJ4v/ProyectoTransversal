# Generated by Django 4.2.1 on 2023-06-19 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webHuertita', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreUser', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=12)),
            ],
        ),
    ]

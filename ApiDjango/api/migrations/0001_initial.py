# Generated by Django 3.2.4 on 2024-01-03 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Usuario', models.CharField(max_length=100)),
                ('Contraseña', models.CharField(max_length=100)),
                ('Correo', models.CharField(max_length=100)),
                ('CP', models.CharField(max_length=100)),
                ('Telefono', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=100)),
            ],
        ),
    ]

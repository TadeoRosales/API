# Generated by Django 3.2.4 on 2024-01-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellidos', models.CharField(max_length=100)),
                ('Usuario', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('Correo', models.CharField(max_length=100)),
                ('CP', models.CharField(max_length=100)),
                ('Telefono', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='registroc',
            old_name='Apellido',
            new_name='Apellidos',
        ),
    ]

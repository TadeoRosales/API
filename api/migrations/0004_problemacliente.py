# Generated by Django 3.2.4 on 2024-01-07 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20240103_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemaCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('ProblemaC', models.CharField(max_length=100)),
                ('Descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]
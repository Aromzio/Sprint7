# Generated by Django 5.1.3 on 2024-11-15 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sucursal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
                ('DNI', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=10)),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sucursal.sucursal')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'Clientes',
            },
        ),
    ]
# Generated by Django 5.1.3 on 2024-11-15 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('tipo_movimiento', models.CharField(max_length=50)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.cuenta')),
            ],
            options={
                'verbose_name': 'Movimiento',
                'verbose_name_plural': 'Movimientos',
                'db_table': 'Movimientos',
            },
        ),
    ]

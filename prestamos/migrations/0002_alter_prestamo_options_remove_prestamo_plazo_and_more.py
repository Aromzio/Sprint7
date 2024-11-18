# Generated by Django 5.1.3 on 2024-11-18 15:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prestamo',
            options={},
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='plazo',
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='tasa_interes',
        ),
        migrations.AddField(
            model_name='prestamo',
            name='aprobado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='tipo_prestamo',
            field=models.CharField(default='Classic', max_length=100),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_inicio',
            field=models.DateField(),
        ),
        migrations.AlterModelTable(
            name='prestamo',
            table=None,
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('BLACK', 'Black'), ('GOLD', 'Gold'), ('CLASSIC', 'Classic')], max_length=10)),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.cliente'),
        ),
    ]

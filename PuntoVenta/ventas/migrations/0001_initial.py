# Generated by Django 5.1 on 2024-10-19 04:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nit_Cui', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('correoElectronico', models.EmailField(blank=True, max_length=200, null=True)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('notas', models.TextField(blank=True, null=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'clientes',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('dpi', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('clave', models.CharField(blank=True, max_length=200, null=True)),
                ('correoElectronico', models.EmailField(blank=True, max_length=200, null=True)),
                ('notas', models.TextField(blank=True, null=True)),
                ('fecha_ingreso', models.DateTimeField(blank=True, null=True)),
                ('rol', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'usuarios',
                'verbose_name_plural': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateField(max_length=255)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('pagado', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('ticket', models.BooleanField(default=True)),
                ('desglosar', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='ventas.cliente')),
            ],
            options={
                'verbose_name': 'egreso',
                'verbose_name_plural': 'egresos',
                'order_with_respect_to': 'fecha_pedido',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=15, null=True)),
                ('descripcion', models.CharField(max_length=255, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('categoria', models.CharField(max_length=100)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=15)),
                ('costo_unitario', models.DecimalField(decimal_places=2, max_digits=15)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'productos',
                'verbose_name_plural': 'productos',
                'order_with_respect_to': 'descripcion',
            },
        ),
        migrations.CreateModel(
            name='ProductosEgreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=20)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('iva', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('entregado', models.BooleanField(default=True)),
                ('devolucion', models.BooleanField(default=False)),
                ('egreso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.egreso')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.producto')),
            ],
            options={
                'verbose_name': 'producto egreso',
                'verbose_name_plural': 'productos egreso',
                'order_with_respect_to': 'created',
            },
        ),
    ]

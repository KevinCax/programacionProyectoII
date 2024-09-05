# Generated by Django 5.1 on 2024-09-03 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('nit', models.CharField(blank=True, max_length=200, unique=True)),
                ('cui', models.CharField(blank=True, max_length=200, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono', models.CharField(blank=True, max_length=200, null=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'clientes',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=255, null=True, unique=True)),
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
    ]

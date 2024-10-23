# Generated by Django 5.1 on 2024-08-19 21:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0002_alter_categorias_descripcion_alter_categorias_nombre_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.FloatField(default=0)),
                ('estado', models.BooleanField(default=False)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('costo', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('id_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compra.compras')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.productos')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('nit', models.CharField(max_length=15)),
                ('dpi', models.CharField(max_length=13)),
                ('empresa', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=100)),
                ('observaciones', models.TextField()),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='compras',
            name='id_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compra.proveedores'),
        ),
    ]

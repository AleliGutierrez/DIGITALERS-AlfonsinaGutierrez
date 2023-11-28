# Generated by Django 3.2.23 on 2023-11-15 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_alter_tag_product_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, verbose_name='País')),
                ('state', models.CharField(max_length=255, verbose_name='Provincia')),
                ('city', models.CharField(max_length=255, verbose_name='Ciudad')),
                ('neighborhood', models.CharField(max_length=255, verbose_name='Barrio')),
                ('street', models.CharField(max_length=255, verbose_name='Calle')),
                ('postal_code', models.CharField(max_length=10, verbose_name='Código postal')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Domicilio',
                'verbose_name_plural': 'Domicilios',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=255, verbose_name='Apellido')),
                ('id_number', models.CharField(max_length=20, verbose_name='DNI')),
                ('phone', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='admin_panel.address', verbose_name='Domicilio')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
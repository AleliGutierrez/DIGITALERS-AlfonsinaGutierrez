# Generated by Django 3.2.23 on 2023-11-12 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='product_list',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='admin_panel.Product'),
        ),
    ]
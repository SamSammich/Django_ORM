# Generated by Django 4.2.3 on 2023-07-23 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='created_at',
        ),
    ]

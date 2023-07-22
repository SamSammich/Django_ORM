# Generated by Django 4.2.3 on 2023-07-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of the product')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of the product')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Photo')),
                ('category', models.CharField(max_length=100, verbose_name='Category')),
                ('purchase_price', models.IntegerField(verbose_name='Purchase price')),
                ('creation_data', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('last_data', models.DateTimeField(auto_now=True, verbose_name='Last modified date')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]

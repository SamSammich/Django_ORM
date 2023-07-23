from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name of the product')
    description = models.TextField(max_length=200, verbose_name='Description')
    image = models.ImageField(upload_to='products/', verbose_name='Photo')
    category = models.CharField(max_length=100, verbose_name='Category')
    purchase_price = models.IntegerField(verbose_name='Purchase price')
    creation_data = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')
    last_data = models.DateTimeField(auto_now=True, verbose_name='Last modified date')

    def __str__(self):
        return f'{self.name}:{self.description}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name of the product')
    description = models.TextField(max_length=200, verbose_name='Description')

    def __str__(self):
        return f'{self.name}:{self.description}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

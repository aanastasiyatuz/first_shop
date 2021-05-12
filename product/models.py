from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string


def gen_slug(string, t=None):
    new_slug = slugify(string, allow_unicode=True)
    if t == 'product':
        add = get_random_string(length=5, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        return new_slug + '_' + add
    return new_slug


class Product(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=37, unique=True, blank=True)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.title, 'product')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug


class ImageProduct(models.Model):
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')


class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=37, unique=True, blank=True)
    image = models.ImageField(upload_to='categories')
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               related_name='children',
                               blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

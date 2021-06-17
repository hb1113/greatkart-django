from django.db import models
from category.models import Category
from django.urls import reverse


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/product')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def get_url(self):
        return reverse('detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


VariationChoices = (
    ('color', 'color'),
    ('size', 'size')
)


class VariationManager(models.Manager):
    def color(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def size(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=VariationChoices)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value

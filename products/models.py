from django.db import models
from django.urls import reverse

class Product(models.Model):
    """
    Model for hydro power products.
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    power_output = models.CharField(max_length=50, help_text="e.g., '1kW - 5kW'")
    water_requirement = models.CharField(max_length=100, help_text="Minimum water flow required")
    dimensions = models.CharField(max_length=100)
    weight = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id])

class ProductFeature(models.Model):
    """
    Model for product features.
    """
    product = models.ForeignKey(Product, related_name='features', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.product.name} - {self.title}"

class ProductImage(models.Model):
    """
    Model for additional product images.
    """
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=100)

    def __str__(self):
        return f"Image for {self.product.name}"

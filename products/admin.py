from django.contrib import admin
from .models import Product, ProductFeature, ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'power_output_kw', 'scalable_to_mw', 'water_requirement_lps')
    list_filter = ('scalable_to_mw', 'is_available')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ('product', 'title')
    list_filter = ('product',)
    search_fields = ('title', 'description')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'alt_text')
    list_filter = ('product',)

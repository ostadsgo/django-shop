from django.contrib import admin

from .models import Category, Product, ProductImage


admin.site.register(Category)
admin.site.register(ProductImage)


class ImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

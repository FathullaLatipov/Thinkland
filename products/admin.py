from django.contrib import admin
from django.utils.html import format_html
from .models import ProductImage, Product, Category


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ['image_tag']
    extra = 1

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="60" />'.format(obj.image.url))
        else:
            return '-'

    image_tag.short_description = 'Image'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
    inlines = [ProductImageInline]


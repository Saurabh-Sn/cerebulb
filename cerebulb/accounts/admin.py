from django.contrib import admin
from .models import User, Product, Category
from django.utils.html import format_html

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_code', 'product_category', 'product_mfg_date', 'product_image']

    list_filter = ('product_category', 'product_mfg_date')

    def product_image(self, obj):
        if obj.product_images:
            return format_html(
                '<img src="{}" width="90" height="90" />', obj.product_images.url)

admin.site.register(User)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
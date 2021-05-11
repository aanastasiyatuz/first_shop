from django.contrib import admin
from .models import *


class ImageProductInlineAdmin(admin.TabularInline):
    model = ImageProduct
    fields = ('image', )
    max_num = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageProductInlineAdmin, ]

admin.site.register(Category)
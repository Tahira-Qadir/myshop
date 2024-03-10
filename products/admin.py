from django.contrib import admin
from .models import Shirt, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ["title", "id", "category", "is_bestselller"]
    list_filter = ["is_bestselller"]
    search_fields = ["title", "category", "brand"]

admin.site.register(Shirt)
admin.site.register(Product, ProductAdmin)
from django.contrib import admin
from .models import Product, Brand, Address, Category, Feedback

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ["title", "id", "is_bestselller"]
    list_filter = ["is_bestselller"]
    search_fields = ["title", "brand"]

# admin.site.register(Shirt)
admin.site.register(Brand)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Feedback)
admin.site.register(Product, ProductAdmin)
from django.db import models

# Create your models here.
class Shirt(models.Model):
    title = models.CharField(max_length=70)
    price = models.PositiveIntegerField()
    # Updating Models
    brand = models.CharField(max_length=40, null=True)  # 1st way null= True
    description = models.TextField(blank=True)          # 2nd way blank=True
    is_bestselller = models.BooleanField(default=False) # 3rd way default=False

    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField() 
    category = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='product-img')  # upload_to='product-img' This location only for this Model
    brand = models.CharField(max_length=50, null=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
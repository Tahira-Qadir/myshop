from django.db import models

# Create your models here.

class Address(models.Model):
    street =  models.CharField(max_length=70)
    city = models.CharField(max_length=20)
    zipcode = models.PositiveIntegerField()
    country = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.city} - {self.country}"
    
class Brand(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)  # one-to-one relationship with Address model

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField() 

    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField() 
    category = models.ManyToManyField(Category)  # Many-to-Many relationship with Category model 
    image = models.ImageField(blank=True, upload_to='product-img')  # upload_to='product-img' This location only for this Model
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True) # One-to-Many relationship with Brand model
    price = models.PositiveIntegerField()
    slug = models.SlugField(blank=True)
    is_bestselller = models.BooleanField(default=False)
    suggestion = models.ManyToManyField('self') #  Many-to-Many Relationship with itself say that same model relationship

    def __str__(self):
        return self.title
    
    def save(self, *args, **kargs):

        super().save(*args, **kargs)
        self.slug = self.id
        super().save(*args, **kargs)

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    rating = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    
    def __str__(self):
        return f"{self.product} - Rating{self.rating}"
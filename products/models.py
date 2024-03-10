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
    
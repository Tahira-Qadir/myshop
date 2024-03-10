from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    birthdate = models.DateField()

    def __str__(self):
        return self.name
    

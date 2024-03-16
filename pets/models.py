from django.db import models

# Create your models here.

class Owner(models.Model):
    name=models.CharField(max_length=80)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=12)

    #Visualización en django admin 
    def __str__(self):
        return self.name
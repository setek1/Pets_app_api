from django.db import models

# Create your models here.

GENDER_CHOICES=[
    ('M', 'Male'),
    ('F','Female'),
]

class Pets(models.Model):
    ownerID=models.ForeignKey('pets_Owner.Owner', on_delete=models.CASCADE)
    nameP=models.CharField(max_length=30)
    ageP=models.IntegerField()
    color=models.CharField(max_length=30)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)

    def __str__(self):
        return f'{self.ownerID} {self.nameP}'
from django.db import models

# Create your models here.

"""class Student(models.Model):
    name =models.CharField(max_length=255)
    image=models.ImageField(default='static/images/default.png')"""

class Products(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    quantity=models.IntegerField()
    image=models.ImageField(upload_to='images/',null=True)


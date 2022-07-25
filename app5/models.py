from ast import Delete
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class batch(models.Model):
    batch_name=models.CharField(max_length=255)
   

class usermember(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    user_batch=models.ForeignKey(batch,on_delete=models.CASCADE)
    user_address=models.CharField(max_length=255)
    user_genter=models.CharField(max_length=255)
    user_mobile=models.IntegerField()
    user_image=models.ImageField(upload_to='images',null=True)

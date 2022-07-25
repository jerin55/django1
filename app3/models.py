from django.db import models

# Create your models here.


class course(models.Model):
    course_name=models.CharField(max_length=255)
    course_fee=models.CharField(max_length=255)


class student(models.Model):
    course=models.ForeignKey(course, on_delete=models.CASCADE,null=True)
    student_name=models.CharField(max_length=255)
    student_address=models.CharField(max_length=255)
    student_age=models.IntegerField()
    join_date=models.DateField()    

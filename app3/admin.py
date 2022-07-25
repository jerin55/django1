from django.contrib import admin

from app3.models import student

# Register your models here.


@admin.register(student)
class studentadmin(admin.ModelAdmin):
    list_display =('id','course','student_name','student_address','student_age','join_date',)
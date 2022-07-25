from . import views
from django.urls import path

urlpatterns = [
   path('two',views.two,name='two'),
   path('cours',views.cours,name='cours'),
   path('addcourse',views.addcourse,name='addcourse'),
   path('students',views.students,name='students'),
   path('addstudent',views.addstudent,name='addstudent'),
   path('showstudent',views.showstudent,name='showstudent')

]

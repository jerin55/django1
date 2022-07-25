from . import views
from django.urls import path

urlpatterns = [
   path('first',views.first,name='first'),
   path('second',views.second,name='second'),
   path('onee',views.onee,name='onee'),
   path('img',views.img,name='img'),
   path('addproduct',views.addproduct,name='addproduct'),
   path('showproduct',views.showproduct,name='showproduct'),
   path('editpage/<int:pk>',views.editpage,name='editpage'),
   path('edit_product/<int:pk>',views.edit_product,name='edit_product'),
   path('delpr/<int:pk>',views.delpr,name='delpr'),
   path('delt/<int:pk>',views.delt,name='delt'),
   path('signup',views.signup,name='signup'),
   path('uslogin',views.uslogin,name='uslogin'),
   path('userceate',views.userceate,name='userceate'),
   path('welcome',views.welcome,name='welcome'),
   path('logout',views.logout,name='logout'),
   path('loginuser',views.loginuser,name='loginuser')
]

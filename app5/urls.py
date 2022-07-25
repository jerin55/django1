from . import views
from django.urls import path

urlpatterns = [
    path('batches',views.batches,name='batches'),
    path('teach',views.teach,name='teach'),
    path('addbatch',views.addbatch,name='addbatch'),
    path('addtech',views.addtech,name='addtech'),
    path('profile',views.profile,name='profile'),
    path('showt',views.showt,name='showt'),
    path('home',views.home,name='home'),
    path('editpr',views.editpr,name='editpr')

   
]

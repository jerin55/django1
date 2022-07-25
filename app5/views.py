
from multiprocessing import context
import os
from django.shortcuts import redirect, render
from app5.models import batch, usermember
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def batches(request):
    if not request.user.is_staff:
        return redirect('uslogin')
    return render (request,'batch.html')


def addbatch(request):
    if request.method=='POST':
        bname=request.POST['batch_name']
       

        bth=batch(
            batch_name=bname,
           
        )
        bth.save()
        return redirect('batches')


def teach(request):
    bat=batch.objects.all()
    context={'bat':bat}
    return render (request,'teacher.html',context)


def addtech(request):
    if request.method=='POST':
        fname=request.POST['first_name'] 
        lname=request.POST['last_name']
        uname=request.POST['username']
        mail=request.POST['email']
        addr=request.POST['user_address']   
        genter=request.POST['user_genter']
        mobile=request.POST['user_mobile']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        sel1=request.POST['sel1']
        batch1=batch.objects.get(id=sel1)
        image=request.FILES.get('user_image')

        if password == cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'already exists')
                return redirect('teach')

            elif User.objects.filter(email=mail).exists():
                messages.info(request,'already exists')
                return redirect('teach')  

            else:
                user=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    email=mail,
                    username=uname,
                    password=password
               )
                user.save()
                u=User.objects.get(id=user.id)

                member=usermember(
                    user_address=addr,
                    user_genter=genter,
                    user_mobile=mobile,
                    user_image=image,
                    user=u,
                    user_batch=batch1,
                )
                member.save()
                return redirect ('uslogin')
        else:
            return render(teach)    

@login_required(login_url='uslogin')
def showt(request):
    sh=usermember.objects.all()
    return render(request,'showteach.html',{'shw':sh})             


@login_required(login_url='uslogin')
def profile(request):
    usr=usermember.objects.filter(user=request.user)
    context={'usr':usr}
    return render(request,'profile.html',context)


def home(request):
    return render (request,'homepage.html')    




def editpr(request):
    if request.method=='POST':
        umember=usermember.objects.get(user=request.user)  
        umember.user.first_name=request.POST.get['first_name']
        umember.user.last_name=request.POST['last_name'] 
        umember.user.email=request.POST['email']
        umember.user.username=request.POST.get['username']
        umember.user_address=request.POST['user_address']
        umember.user_genter=request.POST['user_genter']
        umember.user_mobile=request.POST['user_mobile']
        umember.user_batch.batch_name=request.POST['batch_name']

        if request.FILES.get('user_image') is not None:
            if not umember.user_image == "static/images/default.jpg":
                os.remove(umember.user_image.path)
                umember.user_image=request.FILES['user_image']
            else:
                umember.user_image=request.FILES['user_image']
        else:
            os.remove(umember.user_image.path)
            umember.user_image=request.FILES['user_image']
            umember.user.save()
            umember.save()
            return redirect('profile')
    umember=usermember.objects.get(user=request.user)
    context={'um':umember}
    return render(request,'profile.html',context)                    
   





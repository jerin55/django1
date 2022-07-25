from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login


from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.

def first(request):
    return render(request,'first.html')

def second(request):
    return render(request,'second.html')    


    
def onee(request):
    return render(request,'one.html')

def img(request):
    return render(request,'img.html')    

def addproduct(request):
    if request.method=='POST':
        pname=request.POST['name']
        prname=request.POST['price']
        qname=request.POST['quantity'] 
        image=request.FILES.get('image')

        pr=Products(
            name=pname,
            price=prname,
            quantity=qname,
            image=image
        )   

        pr.save()
        return redirect('showproduct')


def showproduct(request):
    prod=Products.objects.all()
    return render(request,'showproducts.html',{'prdct': prod})


def editpage(request,pk):
    prdts = Products.objects.get(id=pk)
    return render(request,'edidproduct.html',{'prdts': prdts})

def edit_product(request,pk):    
    if request.method=='POST':
        prdcts = Products.objects.get(id=pk)
        prdcts.name = request.POST.get('pname')
        prdcts.Price = request.POST.get('prname')
        prdcts.quantity = request.POST.get('qname')
        prdcts.image = request.FILES.get('image')
        prdcts.save()
        return redirect('showproduct')
        


def delpr(request,pk):
    deltpr=Products.objects.get(id=pk)
    return render(request,'deletepr.html',{'delt': deltpr })


def delt(request,pk):
    ddpr=Products.objects.get(id=pk)
    ddpr.delete()
    return redirect('showproduct') 


def uslogin(request):
    return render(request,'login.html')   


@login_required(login_url='login')
def welcome(request):
    if 'uid' in request.session:
        return render(request,'')     


def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name'] 
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']  

        usr=User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            cpassword=cpassword
        )    

        usr.save()
        print('success')
        return redirect('/')
    else:
        return render(request,'signup.html')



def userceate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']


        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('signup')

            else:
                urs=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                ) 
                urs.save()

                

        else:
            messages.info(request,'password incorrect')    
            return redirect('signup') 
        return redirect('login')    
    else:
        return render(request,'signup.html')   


def loginuser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user =auth.authenticate(username=username,password=password)
        request.session["uid"] = user.id
        
        
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('students')
            else:
                auth.login(request,user)
                messages.info(request, 'welcome' )
                return redirect('profile')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')   

    else:
        return redirect('login') 
  



def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('home')


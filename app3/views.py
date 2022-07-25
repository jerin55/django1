from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required

from app3.models import course
from app3.models import student

# Create your views here.




def two(request):
    return render(request,'two.html')

@login_required(login_url='uslogin')
def cours(request):
    if not request.user.is_staff:
        return redirect('uslogin')
    return render(request,'course.html')

def addcourse(request):
    if request.method=='POST':
        cname=request.POST['course_name']
        fee=request.POST['course_fee']

        crss=course(
            course_name=cname,
            course_fee=fee,
        )
        crss.save()
        return redirect('cours')


@login_required(login_url='uslogin')
def students(request):
    if not request.user.is_staff:
        return redirect('uslogin')
    courses=course.objects.all()
    context={'courses':courses}
    return render(request,'student.html',context)   

@login_required(login_url='uslogin')
def showstudent(request):
    if not request.user.is_staff:
        return redirect('uslogin')
    showstd=student.objects.all()
    return render(request,'showstudent.html',{'sh':showstd})      


def addstudent(request):
    if request.method=='POST':
        student_name=request.POST['student_name']
        student_address=request.POST['student_address']
        student_age=request.POST['student_age']
        join_date=request.POST['join_date']
        sel1=request.POST['sel1']
        course1=course.objects.get(id=sel1)

        std=student(
            student_name=student_name,
            student_address=student_address,
            student_age=student_age,
            join_date=join_date,
            course=course1
        )
        std.save()
        print('success')
        return redirect('showstudent')        

   
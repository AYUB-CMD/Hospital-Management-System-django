from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *

# Non user view start here
def about(request):
    return  render(request, 'about.html')

def contact(request):
    return  render(request, 'contact.html')

def index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')  

# Non user view ends here


# login and logout start here
def LoginAdmin(request):
    error=""
    if request.method =='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if  user.is_staff:
                login(request,user)
                error='no'
            else:
                error='yes'
        except:
               error='yes'   
    d={"error":error}
    return render(request,'login.html',d)         

def logoutAdmin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

# login and logout ends here

# Doctor models view starts here
def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc=Doctor.objects.all()
    d={'doc':doc}
    return render(request,'view_doctor.html',d)


def Add_doctor(request):
    error=""
    if request.method =='POST':
        n=request.POST['d_name']
        c=request.POST['d_contact']
        s=request.POST['d_special']
        
        try:
            Doctor.objects.create(name=n,mobile=c,special=s)
            error='no'

        except:
            error='yes'   
    d={"error":error}
    return render(request,'add_doctor.html',d)         

def Delete_doctor(request,pid):
    if not request.user.is_staff:
        redirect('login')
    doc =Doctor.objects.get(id=pid) 
    doc.delete()
    return redirect('view_doctor')

# Doctor models view ends here


# Patients models view starts here
def View_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat=Patient.objects.all()
    p={'pat':pat}
    return render(request,'view_patient.html',p)

def Add_patient(request):
    error=""
    if request.method =='POST':
        n=request.POST['p_name']
        c=request.POST['p_contact']
        g=request.POST['p_gender']
        a=request.POST['p_address']
        
        try:
            Patient.objects.create(name=n,mobile=c,gender=g,address=a)
            error='no'

        except:
               error='yes'   
    d={"error":error}
    return render(request,'add_patient.html',d)         

def Delete_patient(request,pid):
    if not request.user.is_staff:
        redirect('login')
    pat =Patient.objects.get(id=pid) 
    pat.delete()
    return redirect('view_patient')


# Patients models view ends here


# Appointment models view starts here
def View_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    apt=Appointment.objects.all()
    a={'apt':apt}
    return render(request,'view_appointment.html',a)

def Add_appointment(request):
    error=""
    doctorM=Doctor.objects.all()
    patientM=Patient.objects.all()

    if request.method =='POST':
        d=request.POST['doctor']
        p=request.POST['patient']
        dt=request.POST['date']
        t=request.POST['time']
        doctor=Doctor.objects.filter(name=d).first()
        patient=Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor,patient=patient,date1=dt,time1=t)
            error='no'

        except:
               error='yes'   
    d={"doctor":doctorM,"patient":patientM,"error":error}
    return render(request,'add_appointment.html',d)         

def Delete_appointment(request,pid):
    if not request.user.is_staff:
        redirect('login')
    apt =Appointment.objects.get(id=pid) 
    apt.delete()
    return redirect('view_appointment')


# Appointment models view ends here
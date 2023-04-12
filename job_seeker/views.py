from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Signup
from django.contrib.auth import login, authenticate 
# Create your views here.
def welcome(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        print(type(username))
        print(type(password))
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:5500/job_seeker/Templates/home.html')
        else:
            return HttpResponse('You enter wrong detail')
    return render(request, "index.html")

def hello(request):
    return HttpResponse("hi buddy")

def Register(request):
    if request.method=="POST":
        data=request.POST
        Fname=data['fname']
        Lname=data['lname']
        email=data['email']
        password=data['password1']
        city=data['city']
        country=data['country']
        Username=data['username']
        

        
        obj=Signup(f_name=Fname,l_name=Lname,E_mail=email,Pass1=password,City=city,Country=country,Username=Username)
        obj.save()
        print('User created')
        return redirect('http://127.0.0.1:8000/')
    return render(request, "Register.html")

def forget(request):
    return render(request, "forget.html")
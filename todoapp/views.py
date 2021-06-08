from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Todo
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib.auth.models import User

# Create your views here.

def index1(request):
    if request.user.is_anonymous:
        return redirect("/login")
    todo=Todo.objects.all()
    context={
        'todo':todo
    }
    if request.method=="POST":
        title1=request.POST.get('title')
        time1=request.POST.get('time')
        if title1 is None or title1=="":
            messages.error(request,'Please enter correct action.')
            return redirect('/')
        if time1 is None or time1=="":
            messages.error(request,'Please enter correct time.')
            return redirect('/')
        new_todo=Todo(
            title=title1,
            time=time1
        )
        new_todo.save()
        return redirect('/')
    return render(request,'index1.html',context);


def delete(request,pk):
    deletetodo=Todo.objects.get(id=pk);
    deletetodo.delete()
    return redirect('/')


def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            messages.error(request,'Invalid Credentials.')

            return render(request,'login.html')


    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')


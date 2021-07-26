from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#my scripts
from .forms import CreateUserForm
import os
# Create your views here.


def registerPage(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        form= CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Fue creada tu cuenta '+user+' :)' )
                return render(request, 'login.html')
            else:
                print ('no fue posible crear tu cuenta :(')

        context={'form':form}
        return render(request,'signup.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        if request.method=='POST':
            
            user =authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))

            if user is not None:
                login(request,user)
                return render(request, 'index.html')
            else:
                messages.info(request, 'Nombre de usuario o contraseña esta incorrecta')
            
        context ={} 
        return render(request,'login.html',context)


def logoutPage(request):
    logout(request)
    return render(request, 'index.html')


def welcomePage(request):
    context={}
    return render(request,"bienvenida.html",context)
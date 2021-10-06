from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import customUserCreationForm

# Create your views here.
@login_required(login_url='login/')
def userHome(request):
    return render(request,'users/home.html')

def loginUser(request):    
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'users/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    form = customUserCreationForm()
    if request.method == 'POST':                
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {
        'form':form
    }
    return render(request,'users/register.html',context)
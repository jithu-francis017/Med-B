from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginP(request):
    return render(request, 'login.html', name='login')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi, {username}, your account was created successfully. Login Here...')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html',{'form': form})

@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required()
def profile(request):
    return render(request, 'profile.html')

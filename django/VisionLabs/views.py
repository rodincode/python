from django.shortcuts import render, redirect
from .models import UserProfileInfo
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

def loginview(request):  
       if request.method== 'POST':
              form = AuthenticationForm(data=request.POST)
              if form.is_valid():
                     user = form.get_user()
                     login(request,user)
                     return redirect('users')
       else:
              form = AuthenticationForm()
              
       return render(request, 'Register/index.html',{"form":form})


def signup(request):
       if request.method == 'POST':
              form = SignUpForm(request.POST)
              if form.is_valid():
                     user = form.save()
                     username = form.cleaned_data.get('username')
                     raw_password = form.cleaned_data.get('password1')
                     userok = authenticate(username=username, password=raw_password)
                     login(request, userok)
              return redirect('users')
       else:
              form = SignUpForm()
       return render(request, 'Register/signup.html', {'form': form})

def userview(request):
       x = UserProfileInfo.objects.all()
       return render(request, 'Register/users.html',{'user':x})

def physics_sim(request):
       return render(request, 'Register/physics.html',{})
def chemistry_sim(request):
       return render(request, 'Register/chemistry.html',{})
def biology_sim(request):
       return render(request, 'Register/biology.html',{})       
def home(request):
       return render(request, 'Register/home.html',{})
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
  return render(request,"homes.html")



def signupUser(request):
  if request.user.is_authenticated:
    return redirect('main')
  
  if request.method=="POST":
    username=request.POST['username']
    password=request.POST['password']
    password2=request.POST['password2']
    email=request.POST['email']

    if password==password2:
      if User.objects.filter(username=username).exists():
        messages.info(request,'username already exist')
        return redirect('signup')
      elif User.objects.filter(email=email).exists():
        messages.info(request,'email already exist')
        return redirect('signup')
      else:
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save();
        return redirect('login')
          
    else:
      messages.info(request,'password is not matched')
      return redirect('signup')
  else:
    return render(request,"signup.html")


def loginUser(request):
    
    if request.user.is_authenticated:
      return redirect('main')
    

    if request.method == "POST":


      username=request.POST['username']
      password=request.POST['password']

      try:
        user=User.Objects.get(username=username)
      except:
        print("Username is not found ")

      user=authenticate(request,username=username,password=password)

      if user is not None:
        login(request,user)
        return redirect('main')
      else:
        messages.info(request,"Username or Password is incorrect ")

    return render(request,'login.html')


@login_required(login_url='login')
def main(request):
  return render(request,'main.html')


@login_required(login_url='login')
def logoutUser(request):
  logout(request)
  return redirect('homes')


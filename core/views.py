from django.shortcuts import render
from. models import MYUSERS
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password

# Create your views here.
def signout(request):
    logout(request)
    return redirect ("loginpage")

def home(request):
    return render(request, 'index.html')
def culture(request):
    return render(request, 'Culture.html')
def signup(request):
    
    
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        password=make_password(password)
        username=request.POST.get("username")
        new_user=MYUSERS(first_name=first_name,last_name=last_name,email=email,password=password,username=username)
        new_user.save()
        
        return redirect ("loginpage")
    return render(request, 'Signup.html')
def loginpage(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            print (user)
            login(request,user)
            return redirect ("home")
    return render(request,'login.html')
def Destinations(request):
    return render(request, 'destinations.html')
def About(request):
    return render(request, 'About.html')

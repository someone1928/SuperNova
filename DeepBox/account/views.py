# Importing modules
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"account/signup.html")

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username',"")
        passwd=request.POST.get('passwd',"")
        conf_passwd=request.POST.get('conf_passwd',"")
        checkbox=request.POST.get('checkbox',"")
        all_user=User.objects.all()
        print(list(all_user))
        if passwd==conf_passwd and checkbox=="on":
            user_obj=User.objects.create_user(username=username,password=passwd)
            user_obj.save()
        return redirect("/")

def user_login(request):
    if request.method=="POST":
        login_username=request.POST.get("usernm",'')
        login_passwd=request.POST.get("main_passwd",'')
        user=authenticate(username=login_username,password=login_passwd)

        if user is not None:
            login(request,user)
            messages.success(request,"Logged in !")
            return redirect("/homepage")
        else:
            messages.error(request,"Invalid Data")
            return redirect('')  

def user_logout(request):
    logout(request)
    messages.success(request,'Succesfuly logged out')
    return redirect('/')
    
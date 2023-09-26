from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Post
# Create your views here.

def userhome(request):
    posts=Post.objects.all().order_by("-pk")
    data={'posts':posts}
    return render(request,'homepage/postfeed.html',data)

def profile(request):
    return render(request,'homepage/profile.html')

def post(request):
    if request.method=="POST":
        title_=request.POST.get('title','(Untitled Post)')
        caption_=request.POST.get('caption','(Nothing in caption)')
        user_=request.user
        post_obj=Post(user=user_,caption=caption_,title=title_)
        post_obj.save()
        messages.success(request,"Post uploded sucessfully !")
        return redirect('/homepage')
    else:
        messages.error(request,"Post uploding fail !")
        return redirect('/homepage')



from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogArticle
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    blogs = BlogArticle.objects.all()
    if request.method == 'POST':
        usname = request.POST['username']
        pswd = request.POST['password']
        user = authenticate(username=usname,password=pswd)
        if user is not None:
            login(request,user)
            return render(request,'main.html',{'testvar':'hiikeerthi','blogs':blogs,'user':user})
    return render(request,'main.html',{'testvar':'hiikeerthi','blogs':blogs,'user':None})

def createblog(request):
    blogs = BlogArticle.objects.all()
    newblog = BlogArticle()
    newblog.title = request.POST['title']
    newblog.author = request.user
    newblog.blog_content = request.POST['blog_content']
    newblog.save()
    return render(request,'main.html',{'blogs':blogs,'user':request.user})
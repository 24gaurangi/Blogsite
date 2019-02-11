from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from . import forms
import requests
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    #return HttpResponse('home')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog_list(request):
    blogs = Blog.objects.all().order_by('date')
    return render(request,'bloglist/blog_list.html', {'blogs': blogs})

def blog_details(request, slug):
    blog = Blog.objects.get(slug = slug)
    return render(request, 'bloglist/blog_detail.html', {'blog': blog})

@login_required(login_url='/accounts/login/')
def blog_create(request):
    if request.method == "POST":
        form = forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            #save to db
            new_blog=form.save(commit=False)
            new_blog.author=request.user
            new_blog.save()
            return redirect('bloglist:list')
    else:
        form = forms.CreateBlog()
    return render(request, 'bloglist/blog_create.html',{'form':form})

def rest_view(request):
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    todos = response.json()
    print(todos)
    return render(request, 'bloglist/rest.html', {'todos':todos})

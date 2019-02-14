from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, Comment
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
    blogs = Blog.objects.distinct()
    return render(request,'bloglist/blog_list.html', {'blogs': blogs})

def blog_details(request, slug):
    blog = Blog.objects.get(slug = slug)
    comments = Comment.objects.filter(blog=blog.id).order_by('date')[:5]
    if request.method == "POST":
        print(request.POST)
        if "likes" in request.POST:
            blog.likes.add(request.user)
            print(blog.likes)
            form = forms.CreateComment()
            return render(request, 'bloglist/blog_detail.html', {'blog': blog, 'comments': comments, 'form': form})
        else:
            form = forms.CreateComment(request.POST)
            if form.is_valid():
                #save to db
                new_comment=form.save(commit=False)
                new_comment.blog=blog
                new_comment.author=request.user if request.user else 'guest'
                new_comment.save()
                form = forms.CreateComment()
                return render(request, 'bloglist/blog_detail.html', {'blog': blog, 'comments': comments, 'form':form})
    else:
        form = forms.CreateComment()
    return render(request, 'bloglist/blog_detail.html', {'blog': blog, 'comments':comments, 'form':form })

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


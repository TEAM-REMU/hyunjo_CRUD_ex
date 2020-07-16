from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', { 'blogs': blogs })

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title'] #new.html의 name="title"
    blog.body = request.GET['body'] #new.html의 name="body"
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('home')

# C

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', { 'blog': blog })

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET['title'] #new.html의 name="title"
    blog.body = request.GET['body'] #new.html의 name="body"
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('home')

# R

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('home')

# D
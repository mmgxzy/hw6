from django.shortcuts import render
from .models import Blog

# Create your views here.

def blog(request):
    blogs = Blog.objects.all()

    return render(request, 'blog/blog.html', locals())


def blog_detail(request, id):
    blog = Blog.objects.get(id = id)
    return render(request, 'blog/blog-details.html', locals())
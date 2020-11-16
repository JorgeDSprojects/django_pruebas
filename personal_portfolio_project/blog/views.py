from django.shortcuts import render
from .models import Blog
# Create your views here.
def all_blogs(request):
    Blogs=Blog.objects.order_by('-date')
    return render(request,'blog/all_blogs.html', {'Blogs':Blogs})

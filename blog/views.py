from django.shortcuts import render, get_object_or_404
from blog.models import Blog

# Create your views here.
def allblogs(request):
    blog_post = Blog.objects
    return render(request, 'blog/allblogs.html', {'blog_post': blog_post})



def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    
    return render(request, 'blog/detail.html', {'blog':blog_detail})
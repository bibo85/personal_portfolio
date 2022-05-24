from django.shortcuts import render, get_object_or_404
from blog import models


def all_blogs_view(request):
    blogs = models.Blog.objects.filter(is_published=True)[:5]
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/all_blogs.html', context)


def detail_blog_view(request, blog_id):
    blog = get_object_or_404(models.Blog, pk=blog_id)
    context = {
        'blog': blog,
    }
    return render(request, 'blog/detail_blog.html', context=context)

from django.shortcuts import render
from blog import models


def all_blogs_view(request):
    blogs = models.Blog.objects.filter(is_published=True)[:5]
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/all_blogs.html', context)

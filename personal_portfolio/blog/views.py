from django.shortcuts import render


def all_blogs_view(request):
    return render(request, 'blog/all_blogs.html')


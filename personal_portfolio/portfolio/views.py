from django.shortcuts import render
from portfolio import models


def index_page_view(request):
    projects = models.Project.objects.all()
    context = {
        'text': 'Это мое портфолио',
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', context)


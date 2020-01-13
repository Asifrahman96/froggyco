from django.shortcuts import render, redirect
from django.http import HttpResponse
from projects.models import Project

# Home Page view
def home(request):

    projects_cover = Project.objects.filter(is_published=True).filter(is_cover=True)
    projects_trending = Project.objects.filter(is_published=True).filter(is_trending=True)
    projects_theatre = Project.objects.filter(category="THEATRE").filter(is_published=True)
    projects_movie = Project.objects.filter(category="MOVIE").filter(is_published=True)

    context = {
        'projects_cover':projects_cover,
        'projects_trending':projects_trending,
        'projects_theatre':projects_theatre,
        'projects_movie': projects_movie,
    }
    
    return render(request, 'pages/home.html', context)


# About Page view
def about(request):
    return render(request, 'pages/about.html')

# Talents Page view
def talent(request):
    return render(request, 'pages/talent.html')

# Interaction Page view
def interaction(request):
    return render(request, 'pages/interaction.html')

# Promos Page view
def promos(request):
    return render(request, 'pages/promos.html')

# 404 Page view
def page_404(request):
    return render(request, 'pages/404.html')
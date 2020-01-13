from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Project
from django.contrib.auth.decorators import login_required, user_passes_test
from orders.models import Order

# projects Page view
def projects(request):
    projects = Project.objects.order_by('-year').filter(is_published=True)
    theatres = Project.objects.order_by('-year').filter(is_published=True).filter(category="THEATRE")
    movies = Project.objects.order_by('-year').filter(is_published=True).filter(category="MOVIE")
    context = {
        'projects': projects,
        'theatres':theatres,
        'movies':movies
    }
    return render(request, 'projects/projects.html', context)


def project_detail(request, slug):

    project = get_object_or_404(Project, slug=slug)
    rec_projects = Project.objects.order_by('-year').filter(is_published=True)[:5]
    context = {
        'rec_projects': rec_projects,
        'project': project,
    }
    #checking if user already purchased the project
    if request.method == 'POST':
        project_id = request.POST['project_id']
        project_slug = request.POST['project_slug']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_purchased = Order.objects.all().filter(
                project_id = project_id, user_id=user_id)
            if has_purchased:
                return redirect('/projects/' + project_slug + '/watch')
        return render(request, 'projects/checkout.html', context)

    # Restricting users to access unpublished projects
    check_project = Project.objects.filter(title = project.title)
    if check_project.filter(is_published = False).exists():
        return redirect('404')
    else:
        return render(request, 'projects/project_detail.html', context)


@login_required
def checkout(request, slug):
    if request.user.is_authenticated:
        user_id = request.user.id
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project,
    }
    #checking if user already purchased the project, if already purchased return 404 page
    video_title = Project.objects.filter(title = project.title)
    check_user = Order.objects.filter(user_id=request.user.id).values_list('project_title', flat=True)
    if check_user.filter(project_title = video_title[0]).exists():
        return redirect('404')
    else:
        return render(request, 'projects/checkout.html', context)
        
        
@login_required
def watch(request, slug):
    if request.user.is_authenticated:
        user_id = request.user.id
    video = get_object_or_404(Project, slug=slug)
    context = {
        'video': video
    }
     #checking if user already purchased the project, if not purchased return 404 page
    video_title = Project.objects.filter(title = video.title)
    check_user = Order.objects.filter(user_id=request.user.id).values_list('project_title', flat=True)
    # print(check_user)
    # print(video_title)
    # print(check_user)
    # print(final)
    if check_user.filter(project_title = video_title[0]).exists():
        return render(request, 'projects/project_watch.html', context)
    else:
        return redirect('404')



   


  

  
    
    
 




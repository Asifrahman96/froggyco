from django.urls import path,include
from . import views
    
app_name = 'projects'

urlpatterns = [
    path('',views.projects, name="projects"),
    path('<slug>',views.project_detail, name="project_detail"),
    path('<slug>/checkout',views.checkout, name="checkout"),
    path('<slug>/watch',views.watch, name="watch")
]
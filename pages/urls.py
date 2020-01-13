from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('promos', views.promos, name="promos"),
    path('talent', views.talent, name="talent"),
    path('interaction', views.interaction, name="interaction"),
    path('404', views.page_404, name="404"),
]
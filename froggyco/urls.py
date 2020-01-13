from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('superuser/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
]

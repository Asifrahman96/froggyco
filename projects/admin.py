from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'category',
        'year',
        'created_date',
        'is_cover',
        'is_published',
        'is_trending'
    )
    list_display_links = ('id', 'title')
    list_filter = ('year','category')
    list_editable = ('is_published','is_cover','is_trending')
    search_fields = ('title','director','theatre_type','category')

admin.site.register(Project, ProjectAdmin)
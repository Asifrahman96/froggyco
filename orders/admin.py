from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'project_title',
        'project_category',
        'name',
        'email',
        'price',
        'order_date',
    )
    list_display_links = ('id', 'project_title')
    list_filter = ('order_date','project_category')
    search_fields = ('project_title','name','email','project_category')

admin.site.register(Order, OrderAdmin)
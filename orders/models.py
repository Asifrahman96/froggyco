from django.db import models
from datetime import datetime
from projects.models import Project

class Order(models.Model):
    project_title = models.CharField(max_length=200)
    project_category = models.CharField(max_length=200, blank=True)
    project_slug = models.SlugField(max_length=255, blank=True)
    project_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    price = models.IntegerField()
    photo_card = models.ImageField(blank=True)
    order_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id  = models.IntegerField(blank=True)

    def __str__(self):
        return self.project_title

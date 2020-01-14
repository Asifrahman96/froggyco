from django.db import models
from embed_video.fields import EmbedVideoField

project_choices =(('THEATRE','Theatre'),('SERIES','Series'),('MOVIE','Movie'))

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    project_slug = models.SlugField(max_length=255)
    category = models.CharField(max_length=100, choices=project_choices)
    project_type = models.CharField(max_length=100)
    description = models.TextField(blank=True) 
    year = models.DateField()
    director = models.CharField(max_length=50)
    cast_1 = models.CharField(max_length=50)
    cast_2= models.CharField(max_length=50, blank=True)
    cast_3 = models.CharField(max_length=50, blank=True)
    cast_4 = models.CharField(max_length=50, blank=True)
    cast_5 = models.CharField(max_length=50, blank=True)
    #card image in Home Page & Details Page
    photo_card = models.ImageField(blank=True)
    #carousel Image in Home Page
    photo_cover = models.ImageField(blank=True)
    #Gallery Images in Details Page
    gallery_1 = models.ImageField(blank=True)
    gallery_2 = models.ImageField(blank=True)
    gallery_3 = models.ImageField(blank=True)
    gallery_4 = models.ImageField(blank=True)
    gallery_5 = models.ImageField(blank=True)
    #embed video Field
    trailer = EmbedVideoField(blank=True)  
    #video 
    video = models.FileField(upload_to='videos/', blank=True)
    price = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default = True)
    is_cover = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    
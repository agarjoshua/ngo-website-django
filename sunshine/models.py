from django.db import models
from datetime import date
from datetime import datetime
import datetime
from django.template.defaultfilters import slugify

# Create your models here.
class Carousel(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to="media/carousels")
    slug = models.SlugField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    eventname = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    image = models.ImageField(null=True, upload_to="media/events")
    eventinfo = models.TextField(max_length=850,null=True)
    coodinator = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    @property
    def image_url(self):
        if self.image (self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.eventname

    @property
    def today_event(self):
        tday = date.today()
        return  tday

class Head(models.Model):
    leader = models.CharField(max_length=70,null=True)
    department = models.CharField(max_length=100)
    phone_number = models.IntegerField(null=True)
    images = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.leader

class Ministries(models.Model):
    ministry = models.CharField(max_length=40)
    leader = models.CharField(max_length=70,null=True)
    goals = models.CharField(max_length=80)
    mission = models.CharField(max_length=80)
    vision = models.CharField(max_length=80)
    images = models.ImageField(null=True)
    contacts = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)


    def __str__(self):
        return self.ministry

class Blog(models.Model):
    title = models.CharField(max_length=64,unique=True)
    author = models.CharField(max_length=32)
    images = models.ImageField(null=True)
    content = models.TextField()
    category = models.ForeignKey('sunshine.Category',on_delete=models.CASCADE,null=True)
    slug = models.SlugField(max_length=128,null=True,unique=True)
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)
    publish_on = models.DateField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.headline)
        super(Blog, self).save(*args, **kwargs)
    

class Category(models.Model):
   title = models.CharField(max_length=100, db_index=True)


class Media(models.Model):
    Video = models.FileField (max_length=254)
    Audio = models.FileField (max_length=254,null=True)
    image = models.ImageField(null=True)
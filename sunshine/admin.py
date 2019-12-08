from django.contrib import admin

from .models import Carousel
from .models import Event
from .models import Head
from .models import Ministries
from .models import Blog
from .models import Category
from .models import Media

# Register your models here.
admin.site.register(Carousel)
admin.site.register(Event)
admin.site.register(Head)
admin.site.register(Ministries)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Media)
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'sunshine'

urlpatterns = [
    path('home',views.home ,name='home'),
     path('',views.index , name='index'),
     path('blogs',views.blogs, name='blogs'),
     path('post',views.post, name='post'),
     path('media',views.media, name='media')
]   

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'([\w-]+)/$', views.IndexView.as_view(), name='index'),    
   # url(r'([\w-]+)/([1-9])/$', views.IndexView.as_view(), name='index'),
)

#url(r'^writerbox/([\w-]+)/$', include('writer.urls', namespace='writers')),


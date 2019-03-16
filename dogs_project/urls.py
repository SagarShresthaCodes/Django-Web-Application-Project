from django.conf.urls import url
from . import views

app_name = 'dogs_project'   

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^new_dog/$', views.new_dog, name='new_dog'),    
]


from django.conf.urls import patterns, url
from website import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
    url(r'^addingredient/$', views.addingredient, name='addingredient'),
    url(r'^addnewingredient/$', views.addnewingredient, name='addnewingredient'),
    url(r'^addrecipe/$', views.addrecipe, name='addrecipe'),
)
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.list_of_post, name="post_list"),
    url(r'^blog$', views.blog_list, name="blog_list"),
    #url(r'^(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^blog/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^blog/category/(?P<category_slug>[-\w]+)/$', views.list_of_post_by_category , name='list_of_post_by_category'),
    url(r'^blog/(?P<slug>[-\w]+)/comment/$', views.add_comment,  name='add_comment'),
    url(r'^backend/post/new/$', views.new_post, name='new_post'),
    url(r'^backend/post/$', views.list_of_post_backend, name='list_of_post_backend'),
    url(r'^backend/(?P<slug>[-\w]+)/edit/$', views.edit_post, name='edit_post'),
    url(r'^backend/(?P<slug>[-\w]+)/delete/$', views.delete_post, name='delete_post'),
    
    url(r'^contacto$', views.add_contact, name='add_contact'),
    url(r'^recursos$', views.list_of_post_resource, name='list_of_post_resource'),
    url(r'^herramientas', views.list_of_post_tools, name='list_of_post_tools'),
    url(r'^servicios-web', views.services_web, name='services_web'),


]


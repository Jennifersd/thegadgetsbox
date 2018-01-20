from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.show_list_notchfish, name='show_list_notchfish'),
]

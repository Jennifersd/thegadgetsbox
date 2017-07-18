from django.conf.urls import include, url
from . import views


urlpatterns = [
        url(r'^$', views.products_list, name="products_list"),
        url(r'^category/(?P<category_slug>[-\w]+)/$', views.list_of_product_by_category , name='list_of_product_by_category'),
        url(r'^store/(?P<store_slug>[-\w]+)/$', views.list_of_product_by_store , name='list_of_product_by_store'),

    ]
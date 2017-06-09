from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views

from .sitemap import BlogSitemap
from django.contrib.sitemaps.views import sitemap
 

sitemaps = {
    'blog': BlogSitemap,
}

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('blog.urls', namespace='blog', app_name='blog')),
    
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
        
    url(r'^sitemap\.xml$', sitemap , {'sitemaps': sitemaps}),

    #url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

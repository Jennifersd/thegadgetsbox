from django.shortcuts import render, redirect

from blog.models import Post

import datetime

from django.contrib.sitemaps import Sitemap

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    lastmod = datetime.datetime.now()

    def items(self):
        return post.objects.all()
    
    

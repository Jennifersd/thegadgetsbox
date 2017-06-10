from django.contrib.sitemaps import Sitemap
from blog.models import Post, Category
from django.core.urlresolvers import reverse
from django.utils import timezone
 
class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
 
    def items(self):
        return Post.objects.filter(status='published')
 
    def lastmod(self, obj):
        return obj.published
    

class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
 
    def items(self):
        return Category.objects.all()
 
    def lastmod(self, obj):
        return timezone.now()
    


class StaticSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "daily"
    priority = 0.5

    def items(self):
        # Return list of url names for views to include in sitemap
        return [ 'blog:post_list', 'blog:blog_list', 'blog:add_contact']

    def location(self, item):
        return reverse(item)
    
    def lastmod(self, obj):
        return timezone.now()
   
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User
    
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class Store (models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True)
    #published_categories = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('name', )
        verbose_name = 'store'
        verbose_name_plural = 'stores'
        
    def get_absolute_url(self):
        return reverse('products:list_of_product_by_store', args=[self.slug])
        
    def __str__(self):
        return self.name
        
   

class ProductsCategory (models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True)
    #published_categories = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def get_absolute_url(self):
        return reverse('products:list_of_product_by_category', args=[self.slug])
        
    def __str__(self):
        return self.name
        
    
class Product(models.Model):
  
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    richtextuploads = RichTextUploadingField(config_name='awesome_ckeditor', blank=True)
    #image = models.FileField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_product = models.ImageField(null=True, blank=True)
    
    url_store = models.CharField(max_length=250, blank=True)
    url_video = models.CharField(max_length=250, blank=True)
    category = models.ForeignKey(ProductsCategory)
    store = models.ForeignKey(Store)
    
    code = models.CharField(max_length=250, blank=True)
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    more_prices = models.BooleanField(default=False)
    price = models.IntegerField()
    oldprice = models.IntegerField(null=True)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()
    seo_title = models.CharField(max_length=250)
    seo_description = models.CharField(max_length=250)
    author = models.ForeignKey(User)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')
  
    class Meta:
        ordering = ['-published',]
  
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
        #image = Image.open(self.photo)
        #(width, height) = image.size     
        #size = ( 0, 0)
        #image = image.resize(size, Image.ANTIALIAS)
        #image.save(self.photo.path)
  
   # def get_absolute_url(self):
    #    return reverse('blog:post_detail', args=[self.slug])
    
    def __str__(self):
        return self.title
    
  
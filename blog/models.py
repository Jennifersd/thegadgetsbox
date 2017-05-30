from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User
    
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Category (models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    
    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def get_absoulte_url(self):
        return reverse('blog:list_of_post_by_category', args=[self.slug])
        
    def __str__(self):
        return self.name
        
    
class Post(models.Model):
  
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    richtextuploads = RichTextUploadingField(config_name='awesome_ckeditor', blank=True)
    #image = models.FileField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()
    seo_title = models.CharField(max_length=250)
    seo_description = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name='blog_posts')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')
  
    class Meta:
        ordering = ['-published',]
  
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        #image = Image.open(self.photo)
        #(width, height) = image.size     
        #size = ( 0, 0)
        #image = image.resize(size, Image.ANTIALIAS)
        #image.save(self.photo.path)
  
    def get_absoulte_url(self):
        return reverse('blog:post_detail', args=[self.slug])
    
    def __str__(self):
        return self.title
    
    
    
class Comment (models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    user = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    def approved(self):
        self.approved = True
        self.save()
    
    def __str__(self):
        return self.user

 
class Contact (models.Model):
    email_contact = models.CharField(max_length=250)
    subjet_contact = models.CharField(max_length=250)
    content_contact = models.TextField()
    created_contact = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subjet_contact

  

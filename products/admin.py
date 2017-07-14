from django.contrib import admin
from .models import Product, Category, Store

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fileds = {'slug': ('name',)}
    
admin.site.register(Store, StoreAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fileds = {'slug': ('name',)}
    
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'status')
    list_filter = ('status', 'created', 'published', 'author')
    search_fields = ('title', 'content')
    prepopulated_fileds = {'slug': ('title',)}
    class Media:
       js = ('ckeditor/ckeditor/ckeditor.js')
admin.site.register(Product, ProductAdmin)  

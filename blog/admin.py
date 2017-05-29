from django.contrib import admin
from .models import Post, Category, Comment, Contact

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fileds = {'slug': ('name',)}
    
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'status')
    list_filter = ('status', 'created', 'published', 'author')
    search_fields = ('title', 'contetn')
    prepopulated_fileds = {'slug': ('title',)}
    class Media:
       js = ('ckeditor/ckeditor/ckeditor.js')
admin.site.register(Post, PostAdmin)  

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'approved')
    
admin.site.register(Comment, CommentAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email_contact', 'subjet_contact', 'created_contact')
    
admin.site.register(Contact, ContactAdmin)


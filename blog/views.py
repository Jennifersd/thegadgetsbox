#from urllib import quote_plus
from urllib.parse import quote 

from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import Post, Category, Comment
from django.http import Http404, HttpResponse, HttpResponseRedirect

from django.contrib import messages
from .forms import CommentForm, PostForm, ContactForm

from django.contrib.auth.decorators import login_required

def services_web(request):
    template = 'blog/services/services_web_form.html'
    return render(request, template)

def list_of_post_resource(request):
    template = 'blog/resource/resource_list.html'
    return render(request, template)

def list_of_post_tools(request):
    template = 'blog/tools/tools_list.html'
    return render(request, template)

def blog_list(request):
    #post = Post.objects.filter(updated__lte=timezone.now()).order_by('published')
    categories = Category.objects.all()
    post = Post.objects.order_by('-published')
    query = request.GET.get("q")
    if query:
        post = post.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
            ).distinct()
    paginator = Paginator(post, 3) #cantidad de post
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    template = 'blog/blog_list.html'
    context = {'categories': categories, 'posts': posts, 'page': page}
    return render(request, template, context)

def list_of_post_by_category(request, category_slug):
    categories = Category.objects.all()
    post = Post.objects.filter(status='published')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post = post.filter(category=category)
    query = request.GET.get("q")
    if query:
        post = post.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
            ).distinct()    
    paginator = Paginator(post, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    template = 'blog/category.html'
    context = {'categories': categories, 'posts': posts, 'page': page, 'category': category}
    return render(request, template, context)


def list_of_post(request):
    post = Post.objects.filter(status='published')
    query = request.GET.get("q")
    if query:
        post = post.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
            ).distinct()
    paginator = Paginator(post, 12) #cantidad de post
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    template = 'blog/post_list.html'
    context = {'posts': posts, 'page': page}
    return render(request, template, context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    share_string = quote(post.content)
    context = {'post': post, 'share_string' : share_string}
    if post.status == 'published':        
        template = 'blog/post_detail.html'   
        return render(request, template, context)
    else:
        template = 'blog/post_preview.html'
        return render(request, template, context)

def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = CommentForm()
    template = 'blog/add_comment_to_post.html'
    context = {'form': form}
    return render(request, template, context)

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.success(request, "Successfully Contact")
            return redirect('blog:add_contact')
    else:
        form = ContactForm()
    template = 'blog/contact.html'
    context = {'form': form}
    return render(request, template, context)

#def success(request):
#   return HttpResponse('Success! Thank you for your message.')

#----------------------------------------------------------------
# ---------------------- Backend --------------------------------
#----------------------------------------------------------------


@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()
    template = 'blog/backend/new_post.html'
    context = {'form': form}
    return render(request, template, context)

@login_required
def list_of_post_backend(request):
    post = Post.objects.all()
    paginator = Paginator(post, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    template = 'blog/backend/list_of_post_backend.html'
    context = {'posts': posts, 'page': page}
    return render(request, template, context)  
  
@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:list_of_post_backend')
    else:
        form = PostForm(instance=post)
    template = 'blog/backend/new_post.html'
    context = {'form': form}
    return render(request, template, context)

@login_required
def delete_post(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, "Successfully Delete")
    return redirect('blog:list_of_post_backend')

    
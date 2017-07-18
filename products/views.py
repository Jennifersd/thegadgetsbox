from django.shortcuts import render

#from urllib import quote_plus
from urllib.parse import quote 
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import Product, ProductsCategory, Store
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Product list by store
def list_of_product_by_store(request, store_slug):
    stores = Store.objects.all()
    categories = ProductsCategory.objects.all()
    product = Product.objects.filter(status='published')
    if store_slug:
        store = get_object_or_404(Store, slug=store_slug)
        product = product.filter(store=store)
    query = request.GET.get("q")
    if query:
        product = product.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
            ).distinct()    
    paginator = Paginator(product, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    template = 'products/store.html'
    context = {'stores': stores, 'products': products, 'page': page, 'store': store, 'categories': categories,}
    return render(request, template, context)



# Product list by category
def list_of_product_by_category(request, category_slug):
    categories = ProductsCategory.objects.all()
    stores = Store.objects.all()
    product = Product.objects.filter(status='published')
    if category_slug:
        category = get_object_or_404(ProductsCategory, slug=category_slug)
        product = product.filter(category=category)
    query = request.GET.get("q")
    if query:
        product = product.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
            ).distinct()    
    paginator = Paginator(product, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    template = 'products/category.html'
    context = {'categories': categories, 'products': products, 'page': page, 'category': category, 'stores' : stores}
    return render(request, template, context)



# Product list by product
def products_list(request):
    product = Product.objects.filter(status='published')
    stores = Store.objects.all()
    categories = ProductsCategory.objects.all()
    query = request.GET.get("q")
    if query:
        product = product.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
            ).distinct()
    paginator = Paginator(product, 12) #cantidad de post
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    template = 'products/products_list.html'
    context = {'categories': categories, 'products': products, 'page': page, 'stores': stores}
    return render(request, template, context)

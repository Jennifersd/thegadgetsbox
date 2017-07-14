from django.shortcuts import render

#from urllib import quote_plus
from urllib.parse import quote 
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import Product
from django.http import Http404, HttpResponse, HttpResponseRedirect


# Create your views here.
def products_list(request):
    product = Product.objects.filter(status='published')
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
    context = {'products': products, 'page': page}
    return render(request, template, context)

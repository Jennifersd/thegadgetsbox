from django.shortcuts import render
from django.http import HttpResponse

def show_list_notchfish(request):
    return render(request, 'show_list_notchfish.html')
from django.shortcuts import render
from .models import Market

# Create your views here.

def store(request):
    posts = Market.objects
    return render(request, 'store.html', {'posts': posts})
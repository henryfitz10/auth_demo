from django.shortcuts import render
from .models import Magazine
# Create your views here.

def all_magazines(request):
    magazines = Magazine.objects.all()
    return render(request, "magazines/magazine.html",{"magazines": magazines})
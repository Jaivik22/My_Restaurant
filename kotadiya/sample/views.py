from django.shortcuts import render
from .models import food_items

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    
    foods=food_items.objects.all()

    return render(request,"index.html",{'foods':foods})

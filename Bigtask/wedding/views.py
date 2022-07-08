from importlib.resources import contents
from multiprocessing import context
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from .models import workview, MostPopular, LatestWork, OurFavourites, BehindTheScenes

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    
   Wedding_Images = workview.objects.all()
   context = {'Wedding_Images':Wedding_Images}
   return render(request, "index.html", context)

def work(request):
   # return HttpResponse("working")
   Wedding_Images = workview.objects.all()
   MostPopular_Images = MostPopular.objects.all()
   LatestWork_Images = LatestWork.objects.all()
   OurFavourites_Images = OurFavourites.objects.all()
   BehindTheScenes_Images = BehindTheScenes.objects.all()
   context = {'Wedding_Images':Wedding_Images}
   return render(request, "work.html", context)
from django.shortcuts import render
import requests
from .forms import SubmitEmbed
from .serializer import EmbedSerializer

# Create your views here.

def index(request):
    return render(request,"home/index.html")

def getnews(request):
    #r = request.get('https://api.nytimes.com/svc/topstories/v2/home.json', {'api-key': '7d6470dfcd954000af4d0d8927b8f2d7'})
    #j = r.json()
    #return j
    return render(request,"home/getnews.html")

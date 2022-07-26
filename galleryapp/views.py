from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def uploadpage(request):
    return render(request,"upload.html")

def index(request):
    return render(request,"index.html")
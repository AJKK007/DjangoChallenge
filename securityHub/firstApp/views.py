from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    context = {}
    return render(request,"firstApp/home.html", context)

def about(request):
    context = {}
    return render(request,"firstApp/about.html", context)

def howitworks(request):
    context = {}
    return render(request,"firstApp/how-it-works.html", context)

def contact(request):
    context = {}
    return render(request,"firstApp/contact.html", context)


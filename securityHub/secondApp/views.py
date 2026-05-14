from django.shortcuts import render

# Create your views here.
def dashboard(request):
    context = {}
    return render(request,"secondApp/dashboard.html", context)

def reportincident(request):
    context = {}
    return render(request,"secondApp/report-incident.html", context)

def myreports(request):
    context = {}
    return render(request,"secondApp/my-reports.html", context)

def allincidents(request):
    context = {}
    return render(request,"secondApp/all-incidents.html", context)

def profile(request):
    context = {}
    return render(request,"secondApp/profile.html", context)

def logout(request):
    context = {}
    return render(request,"secondApp/logout.html", context)



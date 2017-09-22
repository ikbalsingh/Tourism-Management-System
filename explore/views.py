from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from authen.models import *
# Create your views here.


def dashboard_home(request):
    if request.user.is_authenticated():
        pr = Profile.objects.get(user=request.user)
        return render(request, 'dashboard.html', {'profile': pr})
    else:
        return redirect('/authen/login/')


def place(request, p):
    if request.user.is_authenticated():
        pr = Profile.objects.get(user=request.user)
        return render(request, 'location.html', {"place": p, "profile": pr})
    else:
        return redirect('/authen/login/')

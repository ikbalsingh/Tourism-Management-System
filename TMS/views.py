from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from authen.models import *
from explore.models import *

def home(request):
     if request.user.is_authenticated():
        pr = Profile.objects.get(user=request.user)
        return render(request, 'index.html', {'profile': pr})

def about(request):
     if request.user.is_authenticated():
        pr = Profile.objects.get(user=request.user)
        return render(request, 'about-us.html', {'profile': pr})



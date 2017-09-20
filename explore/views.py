from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from authen.models import *
# Create your views here.
def dashboard_home(request):
    if request.user.is_authenticated():
        print(request.user)
        user_profile = Profile.objects.get(user = request.user)
        return render(request,'dashboard.html',{'user': user_profile})
    else:
        return HttpResponse('Please login first')

def place(request,p):
    print('ksskks')
    return HttpResponse(p)
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from authen.models import *
from explore.models import *
# Create your views here.


def dashboard_home(request):
    if request.user.is_authenticated():
        pr = Profile.objects.get(user=request.user)
        data = Flyer.objects.all()
        return render(request, 'dashboard.html', {'profile': pr,'allflyers':data})
    else:
        return redirect('/authen/login/')


def place(request, p):
    if request.user.is_authenticated():
         title = request.POST['title']
         desc=request.POST['desc']
         photos = request.POST.get('img')
         videos = request.POST['vid']
         loc = request.POST['loc']
         print(photos)
         #Flyer.objects.all().delete()
         pr = Profile.objects.get(user=request.user)
        

         fly = Flyer.objects.create(title=title, description=desc, location=loc, creater=pr , photos = photos)
            
         fly.save()

         data = Flyer.objects.all()
        

         print(str(pr.user)+" "+title+" "+desc+" "+loc)
         #return render(request, 'dashboard.html',{'allflyers':data})
         return redirect('/dashboard/home/')
    else:
        return redirect('/authen/login/')


def location(request,p):
     data = Flyer.objects.get(title=p) 
     print(data)
     return render(request, 'location.html',{'flyer':data})
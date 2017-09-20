# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Profile
import hashlib
import datetime
import smtplib


# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        photo = request.POST.get('photo')
        if password == confirmpassword:
            user = User.objects.create(username=username)
            user.set_password(request.POST['password'])
            user.save()
        else:
            print('Passwords do not match')
            user = None
        print(user)
        if user is not None:
            hash = hashlib.sha1()
            temp = email + 'hahaha'
            hash.update(temp.encode('utf-8'))
            tp = hash.hexdigest()
            print(tp)   
            user_profile = Profile.objects.create(
                user=user, email=email, profile_pic=photo,confirmhash = tp)
            print(user_profile)
            return HttpResponseRedirect('/authen/login/')
        else:
            return HttpResponse('Some Probem occured')
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/dashboard')
        else:
            return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponse('You havent registered')
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/dashboard')
        else:
            return render(request, 'login.html')


def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)
        return HttpResponse('Succesfully logged out')
    else:
        return HttpResponse('Please login first')


def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        user_profile = Profile.objects.get(email=email)
        if user_profile is not None:

            hash = hashlib.sha1()
            temp = email + 'hahaha'
            hash.update(temp.encode('utf-8'))
            tp = hash.hexdigest()
            print(tp)
            domain = request.get_host()
            scheme = request.is_secure() and "https" or "http"
            TO = email
            SUBJECT = 'TEST MAIL'
            TEXT = "Please Click On The Link To complete registration: {0}://{1}/authen/{2}/resetpassword".format(
                scheme, domain, tp)

            # Gmail Sign In
            gmail_sender = "thecoders000@gmail.com"
            gmail_passwd = "12345ikbal"

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_sender, gmail_passwd)

            BODY = '\r\n'.join(['To: %s' % TO,
                                'From: %s' % gmail_sender,
                                'Subject: %s' % SUBJECT,
                                '', TEXT])

            try:
                server.sendmail(gmail_sender, [TO], BODY)
                print('email sent')
            except:
                print('error sending mail')

            server.quit()

            return HttpResponse('Check your mailbox')

        else:
            return HttpResponse('Email is not registered')

    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/dashboard')
        else:
            return render(request, 'forgotpass.html')


def resetpassword(request, p):
    # print(p)
    # up = Profile.objects.get(confirmhash = p)
    # print(up)
    # return HttpResponse(up)
    if request.method=='POST':
            print(p)
            upass=request.POST.get('upass')
            upass1=request.POST.get('upass1')
            print(upass,upass1)
            if upass==upass1:
                up=Profile.objects.get(confirmhash=p)
                print("user",up.user)
                user = up.user
                a = user.set_password(upass)
                print(a)
                user.save()
                print('hhhhhhh')
                return redirect('/authen/login/')

            else:
                return HttpResponse('Enter password correctly')

    else:
        up=Profile.objects.get(confirmhash = p)
        print(up)
        return render(request,'resetpass.html',{ 'user':up })
        
from django.shortcuts import render,redirect

def faq(request):
    return render(request,'faq.html')

def about(request):
    return render(request,'about-us.html')

def contact(request):
    return render(request,'contact-us.html')

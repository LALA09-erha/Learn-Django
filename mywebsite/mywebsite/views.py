import imp
from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import logout
# from login.models import Login
from django.views.generic import TemplateView



def  Home(request):
    context = {
        'title' : 'Home'
    }
    contextt = {
        'title' : 'Home Sudah Login'
    }
    print(request.user.is_anonymous)
    if request.user.is_anonymous:
        return render (request, 'index.html',context)
    else:
        return render (request, 'index.html',contextt)
    




def Logout(request):
    logout(request)
    return redirect('/')

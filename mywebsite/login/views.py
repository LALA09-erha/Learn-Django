import re
from django.shortcuts import render,redirect
from urllib import request
from django.contrib.auth import *
# Create your views here.
from django.views.generic import TemplateView

def loginView(request):
    # template_name = "login.html"
    context = {
        'title' : 'Login'
    }
    if request.method =="POST":
        username_login = request.POST['username']
        password_login = request.POST['password']
        user = authenticate(request,username =username_login,password = password_login)
        if user is not None:
            login(request,user)
        return redirect('/')
    return render (request, 'login.html', context)

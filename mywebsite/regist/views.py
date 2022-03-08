from django.shortcuts import render
from urllib import request
# Create your views here.
from django.views.generic import TemplateView


def regist(request):
    context = {
        "title" : 'Registrasi'
    }
    return render (request ,'regist.html',context)
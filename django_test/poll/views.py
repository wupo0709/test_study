from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    talk = ""
    name = request.GET.get('name', '')
    for i in range(3):
        talk += "hello,"+name+"\n"
    return HttpResponse(talk)

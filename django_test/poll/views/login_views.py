from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from poll.models.project import Project
from poll.models.module import Module


# Create your views here.


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "" and password == "":
            return render(request, 'index.html', {'error': '用户名密码为空'})
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/manage/')
        else:
            return render(request, 'index.html', {'error': '用户名密码错误'})


@login_required
def manage(request):
    return render(request, 'manage.html')



@login_required
def login_out(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

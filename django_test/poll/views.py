from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth


# Create your views here.
# def set_func(func):
#     def call_func(a):
#         if a.method == "GET":
#             return HttpResponse("错误404")
#         func(a)
#     return call_func


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if username == "" or password == "":
            return render(request, 'index.html', {'error': '用户名密码为空'})

        user = auth.authenticate(username=username, password=password)
        if user is None:
            return render(request, "index.html", {
                "error": "用户名或密码错误"})
        else:
            auth.login(request, user)  # 记录用户的登录状态
            return HttpResponseRedirect("/manage/")


@login_required
def manage(request):
    return render(request, 'manage.html')


@login_required
def login_out(request):
    return HttpResponseRedirect('/index/')

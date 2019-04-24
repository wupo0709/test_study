from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth


# Create your views here.
def sayhello(request):
    if request.method == "GET":
        num1 = request.GET.get("number1","")
        num2 = request.GET.get("number2","")
        num_add = num1+num2
    return render(request,"add.html",{'add_num':'xxxx'})
    # input = request.GET.get("name", "")
    # if input == "":
    #     return HttpResponse("None")
    # else:
    #     return HttpResponse("hello"+input)
    #     # render(request, "index.html", {"name": input_name})


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
def project_manage(request):
    return render(request, 'project.html')


@login_required
def module_manage(request):
    return render(request, 'module.html')


@login_required
def login_out(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

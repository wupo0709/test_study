from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from poll.models.project import Project

@login_required
def project_manage(request):
    project_all = Project.objects.all()
    return render(request, 'project.html', {"projects": project_all,"type":"list"})

def add_project(request):
    if request.method == "GET":
         return render(request,'project.html', {"type":"add"})
    elif request.method == "POST":
        name = request.POST.get("name","")
        describe = request.POST.get("describe","")
        status = request.POST.get("status","")
        if name=="":
            return render(request,'project.html',{"type":"add","name_err":"项目名称不能为空"})
        Project.objects.create(name=name,describe=describe,status=status)
        return HttpResponseRedirect('/project/')

def edit_project(request):
    if request.method == "GET":
        return render(request,'project.html',{"type":"edit"})

def delete_project(request):
    if request.method == "GET":
        return render(request,'project.html',{"type":"delete"})
    
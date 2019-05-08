from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from poll.models.module import Module


@login_required
def module_manage(request):
    module_all = Module.objects.all()
    return render(request, 'module.html', {"modules": module_all})
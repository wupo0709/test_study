from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.


def index(request):
    return render(request, 'add.html')


def jisuan(request):
    if request.method == "POST":
        number1 = request.POST.get("num1", "")
        number2 = request.POST.get("num2", "")
        print(number1, number2)
        result = int(number1)+int(number2)
        return HttpResponse(result)
    else:
        return HttpResponse(request, "add.html")

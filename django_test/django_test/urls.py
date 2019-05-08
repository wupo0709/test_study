"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from poll import views
from js_demo import js_views
from poll.views import login_views
from poll.views import project_views
from poll.views import module_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_views.index),
    path('index/', login_views.index),
    path('manage/', login_views.manage),
    path('out/', login_views.login_out),
    path('accounts/login/', login_views.index),

    path("project/", project_views.project_manage),
    path("project/add_project/", project_views.add_project),
    path("project/edit_project/",project_views.edit_project),
    path("project/delete_project/",project_views.delete_project),

    path("module/", module_views.module_manage),


    path("js/", js_views.index),
    path("js_jisuan/", js_views.jisuan),
]

from django.contrib import admin
from poll.models.project import Project
from poll.models.module import Module
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'status', 'create_time', 'update_time']
    search_fields = ['name', 'describe']


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'create_time']
    search_fields = ['name', 'describe']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)

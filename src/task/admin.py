from django.contrib import admin
from .models import Task, Tag
# from django.templates.default
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Tag)
admin.site.register(Task, TaskAdmin)

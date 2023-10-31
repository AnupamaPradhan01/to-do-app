from django.contrib import admin
from todoapp.models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display=['task','completed']

from django.contrib import admin

from .models import TodoList , TodoItems

# Register your models here.


admin.site.register(TodoItems)
admin.site.register(TodoList)
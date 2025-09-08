from django.contrib import admin
from .models import TodoItem, Book

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(Book)

from dataclasses import field
from pyexpat import model
from django.contrib import admin
from .models import todos
# Register your models here.

class todosAdmin(todos):
    list_display = ('id','title', 'discription', 'is_completed', 'created_at')
    list_filter = ('id','is_completed',)
    fieldsets = (
      ('Task', {'fields': ('id','title', 'discription')}),
      )
  

    search_fields = ('id','title',)
    ordering = ('id')
    filter_horizontal = ('id','is_completed')

admin.site.register(todos)

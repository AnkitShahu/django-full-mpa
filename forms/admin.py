from django.contrib import admin
from .models import MyFormsmodel

# Register your models here.


class FormAdmin(admin.ModelAdmin):
   list_display = ['id', 'name','email', 'phone', 'offi_loc' ]
   
admin.site.register(MyFormsmodel, FormAdmin)
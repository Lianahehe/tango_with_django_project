from django.contrib import admin

#to include the models we previously created(Category & Page)
from django.contrib import admin
from rango.models import Category,Page

admin.site.register(Category)
admin.site.register(Page)
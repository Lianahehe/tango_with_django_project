from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','url')

# customise the admin interface so that it automatically pre-populates the slug field, this class customises the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

#update registration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page,PageAdmin)

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # indicates to Django that we wanna match a string(which is a slug) and to assign it to a varaiable category_name_slug
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    #path('page/', views.index, name='index'),
    path('add_category/', views.add_category, name='add_category'),
]


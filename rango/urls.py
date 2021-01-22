#created to handle the remaining URL string (&map the empty string to the index view)
#imports relevant Django machinery for URL mappings and the views module from rango
#allows us to call the function url and point to the index view 
# #for mapping in urlpatterns


from django.urls import path
from rango import views

app_name = 'rango'

#calls Django's path()function
# 1st param :is the string to match. We used empty string so Django will only find a match if theres nothing after http://127.0.0.1:8000/
# 2nd param : tells Django what view to call if pattern '' is matched
# 3rd(optional) param : (we gave a name to our URL mappings) provides convenient way to reference the view
urlpatterns = [
    path('', views.index, name='index')
]

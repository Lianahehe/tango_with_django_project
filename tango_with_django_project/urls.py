"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
#in order for a user to see your view, we must map a URL to the view
from rango import views

#tells Django to serve static content from MEDIA_URL
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #maps the basic URL to the index view in the rango app
    path('', views.index, name='index'),
    #maps any URLs starting with rango/ to be handled by rango
    path('rango/', include('rango.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
URL configuration for namaproyek project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls import include

from . import dt_jadwal
from django.contrib import admin
from django.urls import path
from namaproyek import views as v

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('',v.index, name='index'),
    path('about_us',v.about_us, name='about_us'),
    path('portovolio',v.portovolio, name='portovolio'),
    path('dt_contact', dt_jadwal.Jadwalku.as_view(), name="dt_contact"),
    path('contact', v.contact, name='contact'),
    path('buku_tamu', v.buku_tamu, name='buku_tamu'),
    path('buku_tamu2', v.buku_tamu2, name='buku_tamu2'),
]

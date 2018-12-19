"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import myapp.views

urlpatterns = [
    url(r'index',myapp.views.Index.as_view()),
    url(r'about',myapp.views.about),
    url(r'copyright',myapp.views.copyright),
    url(r'creators',myapp.views.creators),
    url(r'developers',myapp.views.developers),
    url(r'history',myapp.views.history),
    url(r'movies',myapp.views.movies),
    url(r'news',myapp.views.news),
    url(r'press',myapp.views.press),
    url(r'privacy',myapp.views.privacy),
    url(r'shows',myapp.views.shows),
    url(r'single',myapp.views.single),
    url(r'sports',myapp.views.sports),
    url(r'terms',myapp.views.terms),
    url(r'trys',myapp.views.trys),
    url(r'upload',myapp.views.upload),
    url(r'zhuce',myapp.views.zhuce),



]

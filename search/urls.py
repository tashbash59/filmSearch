from django.urls import path
from django.contrib import admin
from search import views
from .views import *


# URL пути, которые видит пользователь, и функции которые связаны с этими путями
urlpatterns = [
	path('', views.MainPage, name = 'main'),
]


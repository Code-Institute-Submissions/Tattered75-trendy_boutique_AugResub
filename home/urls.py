from django.contrib import admin
from django.urls import path
from . import views
# Lesson code used
urlpatterns = [
    path('', views.index, name='home'),
]

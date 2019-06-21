from django.contrib import admin
from django.urls import include, path
from students.views import *
urlpatterns = [
    path('create/', StudentCreateView.as_view()),]
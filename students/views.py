from django.shortcuts import render
from rest_framework import generics
from students.serializers import StudentDetailSerialzer
# Create your views here.
class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentDetailSerialzer
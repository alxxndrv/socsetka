from django.shortcuts import render
from rest_framework import generics
from students.models import Student
from students.serializers import StudentDetailSerialzer
from students.serializers import StudentListSerializer
# Create your views here.
class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentDetailSerialzer
class StudentListView(generics.ListAPIView):
    serializer_class = StudentListSerializer
    queryset = Student.objects.all()
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentDetailSerialzer
    queryset = Student.objects.all()
from django.shortcuts import render
from .models import students
from .serializers import studentsSerializer

from rest_framework import generics


class studentsListApi(generics.ListAPIView):
    queryset = students.objects.all()
    serializer_class = studentsSerializer
    

from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer

from rest_framework import generics

class BookListApi(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

from rest_framework import generics




class BookListApi(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailApi(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 


class BookDeleteApi(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 

class BookUpdateApi(generics.UpdateAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer 

class BookCreateApi(generics.CreateAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer 

class BookListCreateApi(generics.CreateAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer 

class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# functiion based view
@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
    
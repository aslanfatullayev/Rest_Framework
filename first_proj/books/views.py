from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status




# class BookListApi(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApi(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data ={
            "status": f"Returned {len(books)} books",
            "books": serializer_data
        }

        return Response(data)

# class BookDetailApi(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer 
class BookDetailApi(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            return Response(
                {"status": "Does not Exist",
                 "message": "book is not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_data = BookSerializer(book).data
        data = {
            "status": "Successful",
            "book": serializer_data
        }
        return Response(data)
            

class BookDeleteApi(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 

class BookUpdateApi(generics.UpdateAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer 

# class BookCreateApi(generics.CreateAPIView):
#      queryset = Book.objects.all()
#      serializer_class = BookSerializer 

class BookListCreateApi(generics.CreateAPIView):
      queryset = Book.objects.all()
      serializer_class = BookSerializer 

class BookCreateApi(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            books = serializer.save()
            data = {'status': f"Books are saved to the database",
                    'books': data
                    }
            return Response(data)
        

class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# functiion based view
@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
    
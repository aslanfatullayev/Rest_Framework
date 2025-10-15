from django.urls import path

from .views import BookListApi, book_list_view, BookDetailApi, BookDeleteApi, \
BookUpdateApi, BookCreateApi, BookListCreateApi, BookUpdateDeleteView

urlpatterns = [
    
    path('books/', BookListApi.as_view(),),
    path('bookud/<int:pk>/', BookUpdateDeleteView.as_view()),
    path('booklc/', BookListCreateApi.as_view()),
    path('books/create/', BookCreateApi.as_view()),
    path('books<int:pk>/', BookDetailApi.as_view()),
    path('books<int:pk>/update', BookUpdateApi.as_view()),
    path('books<int:pk>/delete', BookDeleteApi.as_view()),
    # path('books/', book_list_view)
]

from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id','title', 'subtitle', 'author', 'isbn', 'price',)

# Model Serializer
# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     subtitle = serializers.CharField(max_length=200)
#     author = serializers.CharField(max_length=100)
#     isbn = serializers.CharField(max_length=13)
#     price =serializers.IntegerField()
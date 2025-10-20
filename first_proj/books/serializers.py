from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import Book



class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id','title', 'subtitle', 'author', 'isbn', 'price', )

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # check title if it contains only letter chars
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitobni sarlavhasi harflardan tashkil topgan bo'lishi kerak!"
                }
            )
        
        # check title and author from database existence
        if Book.objects.filter(title=title, author=author). exists():
            raise ValidationError(
                {
                    "status":False,
                    "message":"Kitob sarlavhasi va muallifi birxil bo'lgan kitobni yuklay olmaysiz"
                }
            )
        return data
    
    def validate_price(self, price):
        if price < 0 or price > 99999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx notug'ri kiritilgan"
                }
            )
<<<<<<< HEAD
from rest_framework import serializers
from .models import Book

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']
=======
from rest_framework import serializers
from .models import Book

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']
>>>>>>> 9102b10 (blog apps)

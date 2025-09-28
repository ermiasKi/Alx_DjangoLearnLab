from rest_framework import serializers
from .models import Book
from .models import Author

# author serializer converts an Author object into json and vice versa
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


# Book serializer converts an Book object into json and vice versa
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True) # this serializers the author model ( the foriegn field ), only to read ( GET REQUEST )


    def validate_publication_year(self, data):
        if data['publication_year'] > 2025:
            raise serializers.ValidationError("year can not be future")

    class Meta:
        model = Book
        fields = "__all__"
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    publication_year = django_filters.CharFilter(field_name='publication_year')
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = "__all__"
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework
from .filters import BookFilter
from rest_framework import filters

# Create your views here.

@action(detail=False, methods='GET')
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_classes = [BookFilter]

    search_fields = ['title', 'author__name']

    ordering_fields = ['title', 'publication_year']
    

@action(detail=False, methods='GET')
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


@action(detail=False, methods='POST')
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.validated_data["publication_year"] < 2025:
            raise ValidationError("Publication year must be greater than 2025.")
        serializer.save()


@action(detail=False, methods='PATCH')
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


@action(detail=False, methods='DELETE')
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import BookSerializers
from .models import Book

# Create your views here.

class BookList(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    
    queryset = Book.objects.all()
    serializer_class = BookSerializers







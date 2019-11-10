from django.shortcuts import render

from rest_framework.viewsets  import ModelViewSet
from .serializers import ProductSerializer, BookSerializer
from .models import Product, Book

class ProductViewSet(ModelViewSet):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()

class BookViewSet(ModelViewSet):
	serializer_class = BookSerializer
	queryset = Book.objects.all()
from rest_framework import serializers
from .models import Book, Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """Creating serializer class"""
    class Meta:
        model = Category
        fields = ['id', 'title']


class BookSerializer(serializers.ModelSerializer):
    """Creating Book serializer class"""
    class Meta:
        model = Book
        fields = ['id', 'title', 'category', 'author', 'isbn', 'pages', 'price', 'stock', 'description', 'imageUrl', 'status', 'date_created']

        
class ProductSerializer(serializers.ModelSerializer):
    """Creating Product serializer class"""
    class Meta:
        model = Product
        fields = ['id', 'product_tag', 'name', 'category', 'price', 'quantity', 'imageUrl', 'status', 'date_created']
from rest_framework import serializers
from .models import Book, BorrowRequest

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRequest
        fields = '__all__'
        read_only_fields = ['status', 'created_at']

from rest_framework import viewsets, permissions

from books.models import Book
from books.serializers import (
    BookSerializer,
    BookListSerializer
)
from books.premissions import IsAdminOrReadOnly


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action == "list":
            return BookListSerializer
        return BookSerializer

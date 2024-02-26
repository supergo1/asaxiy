from django.shortcuts import render
from .models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def books_list(request):
    books = Book.objects.all()
    data = []
    for book in books:
        data.append(
            {
                "title": book.title,
                "description": book.description,
                "author": book.author.name,
                # "genre": book.genre.first(),
                # "tag": book.tag,
                "price": book.price,
                "image": book.image.url
            }
        )
    return Response(data=data, status=200)
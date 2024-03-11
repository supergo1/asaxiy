from .models import Author, Book, FavoriteAuthor, Wishlist
from account.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from account.jwt_auth import JWTAuthentication 
from .serializers import BookSerializer, BookPostSerializer, BookDetailSerializer, FavoriteAuthorPostSerializer, FavoriteAuthorSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        books = Book.objects.all()
        authors = self.request.GET.getlist('author_id')
        genres = self.request.GET.getlist('genre_id')

        if authors:
            books = books.filter(author_id__in=authors)
        if genres:
            books = books.filter(genre__in=genres)
        return books


class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookPostSerializer
    permission_classes = (IsAdmin,)
    authentication_classes = (JWTAuthentication,)


class BookDeleteAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdmin,)
    authentication_classes = (JWTAuthentication,)


class GetFavoriteAuthorsAPIView(ListAPIView):
    serializer_class = FavoriteAuthorSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        queryset = FavoriteAuthor.objects.filter(user=self.request.user)
        return queryset

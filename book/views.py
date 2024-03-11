from rest_framework.authentication import TokenAuthentication

from .models import *
from account.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from account.jwt_auth import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import BookSerializer, BookDetailSerializer, FavoriteAuthorPostSerializer, FavoriteAuthorSerializer, \
    FeedbackSerializer
from rest_framework.generics import CreateAPIView, ListAPIView

@api_view(['GET'])
def books_list(request):
    books = Book.objects.all()
    authors = request.GET.getlist('author_id')
    genres = request.GET.getlist('genre_id')


    if authors:
        books = books.filter(author_id__in=authors)
    if genres:
        books = books.filter(genre__in=genres)

         

    data = BookSerializer(instance=books, many=True).data
    return Response(data=data, status=200)


@api_view(['GET'])
def book_detail(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    data = BookDetailSerializer(instance=book).data
    return Response(data=data, status=200)


@api_view(['POST'])
@permission_classes([IsAdmin])
@authentication_classes([JWTAuthentication])
def books_create(request):
    data = request.data
    book = Book.objects.create(
        title=data['title'],
        description=data['description'],
        author_id=data['author_id'],
        price=data['price'],
        image=data['image'],
    )

    return Response({"message": "Book created"}, status=201)


@api_view(['DELETE'])
@permission_classes([IsAdmin])
@authentication_classes([JWTAuthentication])
def delete_book(request, book_id):
    Book.objects.filter(pk=book_id).delete()
    return Response({"message": "Kitob o'chirildi"})


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_author_to_favorite(request):
    author_id = request.POST.get('author_id')
    user = request.user
    author = Author.objects.get(pk=author_id)
    fav = FavoriteAuthor.objects.filter(user=user).first()
    if not fav:
        fav = FavoriteAuthor.objects.create(user=user)
    fav.author.add(author)
    fav.save()
    return Response({"message": "muallif yoqtirganlarga qo'shildi"}, status=201)


class AddAuthorToFavorite(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = FavoriteAuthorPostSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data.dict()
        data['user'] = user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"ok"})
        else:
            return Response(serializer.errors, status=400)
    

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_favorite_authors(request):
    favs = FavoriteAuthor.objects.filter(user=request.user).first()
    data = FavoriteAuthorSerializer(instance=favs).data
    return Response(data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def order_book(request):
    user = request.user
    book_id = request.POST.get('book_id')
    is_paid = request.POST.get('is_paid')
    book = BookOrder.objects.filter(id=book_id)
    if book:
        return Response('Already ordered book')
    else:
        book = BookOrder.objects.create(
            user=user,
            book_id=book_id,
            status='want'
        )
        if is_paid or Book.objects.get(id=book_id).price == 0:
            book.status = 'doing'
            book.is_paid = True
            book.save()
            return Response('Successfully ordered book')
        else:
            return Response('Waiting payment')


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def favorite_book(request):
    user = request.user
    book_id = request.GET.get('book_id')
    wishlist = Wishlist.objects.filter(book_id=book_id)
    if not wishlist:
        Wishlist.objects.create(book_id=book_id, user=user)
        return Response('Success')
    else:
        wishlist[0].delete()
        return Response('Deleted')


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def feedback(request):
    user = request.user
    book_id = request.POST.get('book_id')
    rating = request.POST.get('rating')
    text = request.POST.get('text')
    feedback_obj = Feedback.objects.create(
        user=user,
        book_id=book_id,
        rating=rating,
        text=text

    )
    return Response(FeedbackSerializer(feedback_obj).data)


@api_view(['GET'])
def get_feedback(request):
    book_id = request.GET.get('book_id')
    feedback_obj = Feedback.objects.filter(book_id=book_id)
    return Response(FeedbackSerializer(feedback_obj, many=True).data)











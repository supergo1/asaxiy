from django.urls import path
from .views import *
from .class_views import *

urlpatterns = [
    path('books', books_list),
    path('books/<int:book_id>', book_detail),
    path('books/create', books_create),
    path('books/<int:book_id>/delete', delete_book),
    path('add-author-to-favorite', add_author_to_favorite),
    path('add-author-to-favorite-class', AddAuthorToFavorite.as_view()),
    path('get-favorite-authors', get_favorite_authors),
    path('book-list-class', BookListAPIView.as_view()),
    path('book/<int:pk>', BookDetailAPIView.as_view()),
    path('book/create-class/', BookCreateAPIView.as_view()),
    path('book/delete-class/<int:pk>', BookDeleteAPIView.as_view()),
    path('get-favorite-authors-class', GetFavoriteAuthorsAPIView.as_view()),
    path('order-book/', order_book),
    path('wishlist/', favorite_book),
    path('feedback/', feedback),
    path('feedbacks/', get_feedback),
]
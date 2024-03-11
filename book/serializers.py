from book.models import *
from rest_framework import serializers
from account.serializers import UserSerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


class BookPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'price')


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  

    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'price')


class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  
    genre = serializers.SerializerMethodField()
    tag = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'
    
    def get_genre(self, obj):
        data = []
        for genre in obj.genre.all():
            data.append({
                'id': genre.id,
                "name": genre.name
            })
        return data
    
    def get_tag(self, obj):
        data = []
        for genre in obj.tag.all():
            data.append({
                'id': genre.id,
                "name": genre.name
            })
        return data


class FavoriteAuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = FavoriteAuthor
        fields = ('id', 'user', 'author')
        depth = 1


class FavoriteAuthorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteAuthor
        fields = ('id', 'user', 'author')


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'
        depth = 2

  
    
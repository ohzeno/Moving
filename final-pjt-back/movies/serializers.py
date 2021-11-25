from rest_framework import serializers
from .models import *

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ('id', 'name')

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name')

class MovieListSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    directors = DirectorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "overview",
            "release_date",
            "runtime",
            "vote_average",
            "poster_path",
            "backdrop_path",
            "video",
            "actors",
            "genres",
            "directors"
        )
        # read_only_fields = ('like_movies', 'like_users',)


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    directors = DirectorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "overview",
            "release_date",
            "runtime",
            "vote_average",
            "poster_path",
            "backdrop_path",
            "video",
            "actors",
            "genres",
            "directors"
        )
        # read_only_fields = ('like_movies', 'like_users',)

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'rate',)
        read_only_fields = ('user', 'movie')

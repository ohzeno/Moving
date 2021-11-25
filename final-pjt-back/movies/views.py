from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer, MovieListSerializer, ActorSerializer, GenreSerializer, DirectorSerializer, RatingSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# from django.shortcuts import render, get_list_or_404


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_main(request):
    movies =Movie.objects.order_by("-release_date")[:30]
    # movies = Movie.objects.all()[:30]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
@permission_classes([AllowAny])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def actors_list(request):
    actors = Actor.objects.all()[:30]
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def directors_list(request):
    directors = Director.objects.all()[:30]
    serializer = DirectorSerializer(directors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def director_detail(request, director_pk):
    director = get_object_or_404(Director, pk=director_pk)
    serializer = GenreSerializer(director)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def genres_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def rating_list_create(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method=='GET':
        ratings = movie.ratings.all()
        serializer= RatingSerializer(ratings, many=True)
        return Response(serializer.data)
    else:
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([AllowAny])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def rating_delete(request, rating_pk):
    rating = get_object_or_404(Rating, pk=rating_pk)
    rating.delete()
    return Response({'id': rating_pk})

@api_view(['GET', 'POST', 'PUT'])
# @permission_classes([AllowAny])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def rates(request, movie_pk):
    movie = get_object_or_404(Movie, id=movie_pk)
    rating = Rating.objects.filter(user__pk=request.user.pk, movie__pk=movie_pk).first()
    # print(rating)
    if request.method == 'GET':
        # print('get들어옴')
        serializer = RatingSerializer(rating)
        print(serializer)
        return Response(serializer.data)
    elif request.method == "POST":
        # print('post 들어옴')
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        # print('put 들어옴')
        serializer = RatingSerializer(rating, data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            # print('밸리드들어옴')
            serializer.save()
            # 3. for문을 통해 각 장르 아이디들에 대해 유저장르점수 객체 업데이트
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)

# @api_view(['GET'])
# @permission_classes([AllowAny])
# # @authentication_classes([JSONWebTokenAuthentication])
# # @permission_classes([IsAuthenticated])
# def rate(request, genre_pk):
#     genre = get_object_or_404(Genre, pk=genre_pk)
#     serializer = GenreSerializer(genre)
#     return Response(serializer.data)


@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def recommend(request):
    movies = Movie.objects.order_by("?")[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def recommend_genre(request, genre_pk):
    movies = Movie.objects.filter(genres=genre_pk).order_by("?")[:21]
    # movies = Movie.objects.filter(title='The Man Nobody Knew: In Search of My Father, CIA Spymaster William Colby').order_by("?")[:10]
    # movie = get_object_or_404(Movie, pk='189')
    # print(movies[0])
    # serializer = MovieSerializer(movie)
    # return Response(serializer.data)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def movie_find(request, word):
    movies = Movie.objects.filter(title__contains=word)
    # print(movies)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
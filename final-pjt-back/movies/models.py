from django.db import models
from django.db.models.fields.related import ForeignKey
from django.conf import settings

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=50)

class Director(models.Model):
    name = models.CharField(max_length=50)

class Genre(models.Model):
    name = models.CharField(max_length=50)

    
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    runtime = models.CharField(max_length=30)
    vote_average = models.FloatField()
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    video = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='movies')
    directors = models.ManyToManyField(Director, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies')

class Rating(models.Model):
    RANKS = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    rate = models.IntegerField(choices=RANKS, default=5)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_rates')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_rates')
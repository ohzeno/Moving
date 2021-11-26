import os
import django
import sys


# system setup
os.chdir('.')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'back.settings') 

django.setup() # 파이썬 파일에서 django를 실행 시킬수 있다.

import pandas as pd
from movies.models import Actor, Director, Genre, Movie


def str_to_list(word):
    word = word.replace('[', '')
    word = word.replace('\'', '')
    word = word.replace(']', '')
    try:
        res = list(map(str, word.split(', ')))
        return res
    except Exception as err:
        print(err)
        print(word)
        print(type(word))
        return 0

df = pd.read_csv('../back/fixtures/movies.csv', index_col='id')
# print(df)

for i in range(len(df)):
    t = df['genres'][df.index[i]]
    genres = str_to_list(t)
    if genres == 0:
        break
    for genre in genres:
        if not Genre.objects.filter(name=genre):
            Genre.objects.create(name=genre)
    print(f'genres {i} 성공')

for i in range(len(df)):
    t = df['actors'][df.index[i]]
    actors = str_to_list(t)
    if actors == 0:
        break
    for actor in actors:
        if not Actor.objects.filter(name=actor):
            Actor.objects.create(name=actor)
    print(f'actors {i} 성공')

for i in range(len(df)):
    t = df['director'][df.index[i]]
    directors = str_to_list(t)
    if directors == 0:
        break
    for director in directors:
        if not Director.objects.filter(name=director):
            Director.objects.create(name=director)
    print(f'director {i} 성공')

for i in range(len(df)):
    title = df['title'][df.index[i]]
    overview = df['overview'][df.index[i]]
    release_date = df['release_date'][df.index[i]]
    runtime = df['runtime'][df.index[i]]
    vote_average = df['vote_average'][df.index[i]]
    poster_path = df['poster_path'][df.index[i]]
    backdrop_path = df['backdrop_path'][df.index[i]]
    video = df['youtube_link'][df.index[i]]
    # if not Movie.objects.filter(
        # title=title,
        # overview=overview,
        # release_date=release_date,
        # runtime=runtime,
        # vote_average=vote_average,
        # poster_path=poster_path,
        # backdrop_path=backdrop_path,
        # video=video
        # ):
    movie,_ = Movie.objects.get_or_create(
        title=title,
        overview=overview,
        release_date=release_date,
        runtime=runtime,
        vote_average=vote_average,
        poster_path=poster_path,
        backdrop_path=backdrop_path,
        video=video
    )
    actors = df['actors'][df.index[i]]
    directors = df['director'][df.index[i]]
    genres = df['genres'][df.index[i]]
    actors = str_to_list(actors)
    directors = str_to_list(directors)
    genres = str_to_list(genres)
    for actor in actors:
        ac = Actor.objects.get(name=actor)
        movie.actors.add(ac)
    for director in directors:
        di = Director.objects.get(name=director)
        movie.directors.add(di)
    for genre in genres:
        ge = Genre.objects.get(name=genre)
        movie.genres.add(ge)
    print(f'Movie에 {i}번째 정보 담기 성공')


# print(list(df['genres'][df.index[0]])[0])
# print(list(df['genres'][df.index[0]])[1])
# print(len(list(df['genres'][df.index[0]])))
# print(df['release_date'][df.index[1]])

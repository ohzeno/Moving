from django.urls import path
from . import views

# app_name="movies"

urlpatterns = [
    path('', views.movie_main),
    path('find/<str:word>/', views.movie_find),
    path('actors/', views.actors_list),
    path('directors/', views.directors_list),
    path('genres/', views.genres_list),
    path('<int:movie_pk>', views.movie_detail),
    # path('actors/<int:actor_pk>', views.actor_detail),
    # path('genres/<int:genre_pk>', views.genre_detail),
    path('directors/<int:director_pk>', views.director_detail),
    path('<int:movie_id>/rating_list_create/', views.rating_list_create),
    path('<int:rating_pk>/rating_delete/', views.rating_delete),
    path('recommend/', views.recommend),
    path('recommend/genre/<int:genre_pk>', views.recommend_genre),
    path('<int:movie_pk>/rates', views.rates),
]
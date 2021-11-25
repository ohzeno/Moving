from django.urls import path
from . import views

app_name="community"

urlpatterns = [
    path('', views.get_review_list),
    path('create/', views.review_create),
    path('<int:review_pk>/', views.review_detail),
    path('<int:review_pk>/comments/', views.comment_list_or_create),
    path('<int:review_pk>/comments/create/', views.comment_list_or_create),
    path('<int:comment_pk>/comments/delete/', views.comment_update_or_delete),
    path('<int:comment_pk>/comments/update/', views.comment_update_or_delete),
]
from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('api-token-auth/', obtain_jwt_token),
]
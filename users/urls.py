from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('profile/', views.update_user_and_profile, name='profile'),
]

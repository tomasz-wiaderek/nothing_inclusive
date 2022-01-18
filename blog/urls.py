from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('author/<int:pk>', views.list_authors_posts, name='posts-by-author'),
    path('category/<str:name>', views.list_categorys_posts, name='posts-by-category'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.post_detail_view, name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('image/', views.ImageListView.as_view(), name='image-list'),
    path('image/new/', views.ImageCreateView.as_view(), name='image-create'),
    path('image/<slug:slug>/', views.ImageDetailView.as_view(), name='image-detail'),
    path('image/<slug:slug>/update/', views.ImageUpdateView.as_view(), name='image-update'),
    path('image/<slug:slug>/delate/', views.ImageDeleteView.as_view(), name='image-delete'),
]

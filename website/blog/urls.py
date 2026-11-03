from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.get_post, name='post_detail'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('contact/', views.contact, name='contact'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/update/<int:id>/', views.post_update, name='post_update'),
]

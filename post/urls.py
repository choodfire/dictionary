from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:id>/', views.post, name='post'),
    path('results/', views.search, name='search'),
    path('results/<int:year>/<int:month>/', views.searchByDate, name='searchByDate'),
    # path('create/', views.createPost, name='createPost'),
    path('create/', views.CreatePost.as_view(), name='createPost'),
    path('edit/<int:pk>/', views.EditPost.as_view(), name='editPost'),
    path('delete/<int:pk>/', views.DeletePost.as_view(), name='deletePost'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('post/<int:id>/', views.post, name='post'),
    path('results/', views.search, name='search'),
    path('results/<int:year>/<int:month>/', views.searchByDate, name='searchByDate'),
    path('about/', views.about, name='about'),
    path('create/', views.createPost, name='createPost'),
    path('edit/<int:id>/', views.editPost, name='editPost'),
    path('delete/<int:id>/', views.deletePost, name='deletePost'),
]
from django.urls import path
from . import views


urlpatterns = [
    path('post/<int:pk>/', views.PostView.as_view(), name='post'),
    # path('results/', views.search, name='search'),
    path('results/', views.Search.as_view(), name='search'),
    path('results/<int:year>/<int:month>/', views.SearchByDate.as_view(month_format='%m'), name='searchByDate'),
    path('create/', views.CreatePost.as_view(), name='createPost'),
    path('edit/<int:pk>/', views.EditPost.as_view(), name='editPost'),
    path('delete/<int:pk>/', views.DeletePost.as_view(), name='deletePost'),
]

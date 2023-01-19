from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('post/<int:id>/', views.post, name='post'),
    path('results', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('create/createResult/', views.createResult, name='createResult'),
]
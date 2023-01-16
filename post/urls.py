from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    # path('post/<int:id>/', views.Post, name='Post')
]
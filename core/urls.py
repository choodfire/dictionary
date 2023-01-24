from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='mainPage'),
    path('about/', views.About.as_view(), name='about'),
]

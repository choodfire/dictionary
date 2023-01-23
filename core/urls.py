from django.urls import path
from . import views

urlpatterns = [
    # path('', views.mainPage, name='mainPage'),
    path('', views.MainPage.as_view(), name='mainPage'),
    # path('about/', views.about, name='about'),
    path('about/', views.About.as_view(), name='about'),
]
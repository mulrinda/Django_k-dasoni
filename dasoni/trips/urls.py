from django.urls import path
from . import views

app_name = 'trips'

urlpatterns = [
    path('spotchart', views.spotchart, name='spotchart'),
    path('share/', views.share, name='share'),
    path('create/', views.create, name='create'),
    path('dasonitour/', views.dasonitour, name='dasonitour'),
    path('photo/', views.photo, name='photo'),
    path('social/', views.social, name='social'),
]
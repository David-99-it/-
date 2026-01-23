from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply, name='apply'),
    path('about/', views.about, name='about'),
    path('news/', views.news_list, name='news_list'),
    path('jobs/', views.jobs, name='jobs'),
    path('science/', views.science, name='science'),
    path('courses/', views.courses, name='courses'),
]

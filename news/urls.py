from django.urls import path
from .views import news_detail

urlpatterns = [
    path('<int:pk>/', news_detail, name='news_detail'),
]

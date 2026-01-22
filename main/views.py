from news.models import News
from django.shortcuts import render, get_object_or_404

def home(request):
    last_news = News.objects.filter(is_active=True).order_by('-created_at')[:3]
    return render(request, 'main/home.html', {
        'last_news': last_news
    })



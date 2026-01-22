from django.shortcuts import render, get_object_or_404
from news.models import News

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk, is_active=True)
    return render(request, 'news/news_detail.html', {
        'news': news
    })

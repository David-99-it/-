from news.models import News
from django.shortcuts import render, get_object_or_404

def home(request):
    last_news = News.objects.filter(is_active=True).order_by('-created_at')[:3]
    return render(request, 'main/home.html', {
        'last_news': last_news
    })
def about(request):
    return render(request, 'main/about.html')

def apply(request):
    return render(request, 'main/apply.html')

def news_list(request):
    news_list = News.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'main/news.html', {
        'news_list': news_list
    })

def jobs(request):
    return render(request, 'main/jobs.html')

def science(request):
    return render(request, 'main/science.html')

def courses(request):
    return render(request, 'main/courses.html')
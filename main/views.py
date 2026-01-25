from news.models import News
from jobs.models import Vacancy
from django.shortcuts import render, get_object_or_404
from django.db.models import Q


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

def jobs(request):
    vacancies = Vacancy.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'main/jobs.html', {
        'vacancies': vacancies
    })

def vacancy_apply(request):
    # просто покажем страницу с формой Google
    return render(request, 'main/vacancy_apply.html')

def search_results(request):
    query = request.GET.get('q', '')
    news_results = News.objects.filter(
        Q(title__icontains=query) | Q(text__icontains=query)
    ) if query else News.objects.none()
    
    vacancy_results = Vacancy.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    ) if query else Vacancy.objects.none()

    return render(request, 'main/search_results.html', {
        'query': query,
        'news_results': news_results,
        'vacancy_results': vacancy_results,
    })

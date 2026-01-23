from django.shortcuts import render, get_object_or_404
from news.models import News

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    referer = request.META.get('HTTP_REFERER', '/news/')  # если нет реферера, идем на /news/

    # Берём якорь, если передали через GET
    anchor = request.GET.get('anchor')
    if anchor:
        back_url = f"{referer}#{anchor}"
    else:
        back_url = referer

    return render(request, 'news/news_detail.html', {
        'news': news,
        'back_url': back_url
    })

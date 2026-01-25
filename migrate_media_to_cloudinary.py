import os
from django.core.files import File
import django
import cloudinary.uploader
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from news.models import News

for news in News.objects.all():
    if news.image:  # если у новости есть картинка
        # получаем путь к файлу на диске
        local_path = os.path.join(settings.MEDIA_ROOT, news.image.name)
        if os.path.exists(local_path):
            try:
                # загружаем на Cloudinary
                result = cloudinary.uploader.upload(local_path, folder="news")
                # сохраняем только URL Cloudinary
                news.image = result['secure_url']
                news.save()
                print(f"Uploaded {local_path} -> {news.image}")
            except Exception as e:
                print(f"Failed {local_path}: {e}")
        else:
            print(f"File not found: {local_path}")

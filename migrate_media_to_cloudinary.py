import os
import django
import cloudinary
import cloudinary.uploader
from django.conf import settings

# 1. Настройка Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from news.models import News

# 2. Настройка Cloudinary
cloudinary.config(
    cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
    api_secret=settings.CLOUDINARY_STORAGE['API_SECRET'],
)

# 3. Миграция всех локальных изображений
for news in News.objects.all():
    if news.image:
        # Если image.url уже содержит https://, значит картинка уже на Cloudinary
        if news.image.url.startswith("http"):
            print(f"Already on Cloudinary, skipping: {news.image.url}")
            continue

        # Путь к файлу на диске
        local_path = os.path.join(settings.MEDIA_ROOT, news.image.name)

        # Проверяем, что файл реально существует
        if not os.path.exists(local_path):
            print(f"File not found: {local_path}")
            continue

        try:
            # Загружаем на Cloudinary в папку "news"
            result = cloudinary.uploader.upload(local_path, folder="news")
            # Сохраняем новый URL в базе
            news.image = result['secure_url']
            news.save()
            print(f"Uploaded {local_path} -> {news.image}")
        except Exception as e:
            print(f"Failed {local_path}: {e}")

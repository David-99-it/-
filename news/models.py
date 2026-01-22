from django.db import models

class News(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст новости")
    image = models.ImageField("Картинка", upload_to='news/', blank=True, null=True)
    is_active = models.BooleanField("Актуально", default=True)
    created_at = models.DateTimeField("Дата публикации", auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # новые сверху

    def __str__(self):
        return self.title

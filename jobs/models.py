
from django.db import models

class Vacancy(models.Model):
    title = models.CharField("Название вакансии", max_length=200)
    description = models.TextField("Описание")
    is_active = models.BooleanField("Активна", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


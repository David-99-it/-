# jobs/views.py
from django.shortcuts import render
from .models import Vacancy

def vacancies(request):
    vacancies = Vacancy.objects.filter(is_active=True).order_by("-created_at")
    return render(request, "jobs/vacancies.html", {
        "vacancies": vacancies
    })

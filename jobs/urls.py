# jobs/urls.py
from django.urls import path, include
from .views import vacancies

urlpatterns = [
    path("", vacancies, name="vacancies"),
    path("vacancies/", include("jobs.urls")),
]

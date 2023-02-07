from django.urls import path

from models_exercise.departments.views import show_all_departments

urlpatterns = [
    path('', show_all_departments, name='departments'),
]

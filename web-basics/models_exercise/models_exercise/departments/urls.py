from django.urls import path

from models_exercise.departments.views import show_all_departments, add_new_name

urlpatterns = [
    path('', show_all_departments, name='departments'),
    path('add/', add_new_name, name='new-name')
]

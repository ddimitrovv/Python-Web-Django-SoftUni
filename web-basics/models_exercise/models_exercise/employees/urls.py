from django.urls import path

from models_exercise.employees.views import add_new_employee, update_employee

urlpatterns = [
    path('add/', add_new_employee, name='add-employee'),
    path('update/<int:pk>', update_employee, name='update-employee')
]

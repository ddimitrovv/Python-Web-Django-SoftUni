from django.urls import path

from departments.app import views

urlpatterns = [
    path('', views.show_department)
]

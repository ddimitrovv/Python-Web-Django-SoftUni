from django.urls import path

from djangoProject.employee import views

urlpatterns = [
    path('', views.employee_info)
]

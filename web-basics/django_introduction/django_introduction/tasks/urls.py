from django.urls import path

from django_introduction.tasks import views

urlpatterns = [
    path('', views.index)
]
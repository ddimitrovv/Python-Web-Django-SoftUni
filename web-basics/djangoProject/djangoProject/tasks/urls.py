from django.urls import path

from djangoProject.tasks import views

urlpatterns = [
    path('', views.index)
]
from django.urls import path

from djangoProject.departments import views

urlpatterns = [
    path('', views.show_department),
    path('<int:department_id>/', views.show_department_by_id),
]

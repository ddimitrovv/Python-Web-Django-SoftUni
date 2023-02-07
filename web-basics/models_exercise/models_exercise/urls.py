from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('models_exercise.employees.urls')),
    path('departments/', include('models_exercise.departments.urls')),
]

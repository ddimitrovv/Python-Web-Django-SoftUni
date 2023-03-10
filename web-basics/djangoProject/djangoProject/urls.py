from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangoProject.tasks.urls')),
    path('departments/', include('djangoProject.departments.urls')),
    path('employees/', include('djangoProject.employee.urls')),

]

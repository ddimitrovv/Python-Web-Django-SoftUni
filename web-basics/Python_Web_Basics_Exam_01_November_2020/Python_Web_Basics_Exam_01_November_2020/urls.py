from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Python_Web_Basics_Exam_01_November_2020.recipes.urls')),
]

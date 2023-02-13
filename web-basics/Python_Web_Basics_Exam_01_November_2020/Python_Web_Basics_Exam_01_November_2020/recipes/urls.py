from django.urls import path

from Python_Web_Basics_Exam_01_November_2020.recipes.views import index

urlpatterns = [
    path('', index, name='main-page'),
]

from django.urls import path

from Python_Web_Basics_Exam_01_November_2020.recipes.views import index, create_recipe, edit_recipe, delete_recipe, \
    details_recipe

urlpatterns = [
    path('', index, name='main-page'),
    path('details/<int:pk>/', details_recipe, name='details recipe'),
    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
]

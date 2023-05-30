from django.urls import path

from Recipes.web.views import home_view, create_recipe, details_recipe, edit_recipe, delete_recipe

urlpatterns = (
    path('', home_view, name='home'),
    path('create/', create_recipe, name='create recipe'),
    path('details/<int:pk>/', details_recipe, name='details recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
)

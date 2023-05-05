from django.urls import path

from Online_Library.web.views import home_view, add_book, profile_details, profile_edit, profile_delete, details_book, \
    edit_book, delete_book

urlpatterns = (
    path('', home_view, name='home'),
    path('add/', add_book, name='add book'),
    path('profile/', profile_details, name='profile details'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete'),
    path('details/<int:pk>/', details_book, name='book details'),
    path('edit/<int:pk>/', edit_book, name='book edit'),
    path('delete/<int:pk>', delete_book, name='book delete'),
)


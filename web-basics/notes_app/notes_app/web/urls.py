from django.urls import path

from notes_app.web.views import profile_details, home_view, create_note, edit_note, note_details, note_delete, \
    delete_profile

urlpatterns = (
    path('', home_view, name='home'),
    path('profile/', profile_details, name='profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('add/', create_note, name='create note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('details/<int:pk>/', note_details, name='note details'),
    path('delete/<int:pk>/', note_delete, name='note delete')
)


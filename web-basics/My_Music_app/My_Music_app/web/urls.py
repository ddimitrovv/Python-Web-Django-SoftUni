from django.urls import path, include

from My_Music_app.web.views import home_view, profile_details, profile_delete, add_album, details_album, edit_album, \
    delete_album

urlpatterns = (
    path('', home_view, name='home'),
    path('profile/', include([
        path('details/', profile_details, name='profile details'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
    path('album/', include([
        path('add/', add_album, name='add album'),
        path('details/<int:pk>/', details_album, name='album details'),
        path('edit/<int:pk>/', edit_album, name='album edit'),
        path('delete/<int:pk>/', delete_album, name='album delete'),
    ])),
)

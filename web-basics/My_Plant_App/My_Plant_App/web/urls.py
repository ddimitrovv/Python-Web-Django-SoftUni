from django.urls import path, include

from My_Plant_App.web.views import home_view, add_profile, catalogue, create_plant, details_plant, profile_details, \
    edit_plant, delete_plant, edit_profile, delete_profile

urlpatterns = (
    path('', home_view, name='home'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', add_profile, name='add profile'),
        path('details/', profile_details, name='profile details'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile')
    ])),
    path('create/', create_plant, name='create plant'),
    path('details/<int:pk>/', details_plant, name='details plant'),
    path('edit/<int:pk>/', edit_plant, name='edit plant'),
    path('delete/<int:pk>/', delete_plant, name='delete plant'),
)

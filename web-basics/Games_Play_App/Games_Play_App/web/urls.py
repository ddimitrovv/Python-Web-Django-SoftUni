from django.urls import path

from Games_Play_App.web.views import home_view, add_profile, create_game, dashboard, \
    profile_details, edit_game, details_game, delete_game, edit_profile, delete_profile

urlpatterns = (
    path('', home_view, name='home'),
    path('profile/create/', add_profile, name='add profile'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('game/create/', create_game, name='create game'),
    path('game/edit/<int:pk>/', edit_game, name='edit game'),
    path('game/details/<int:pk>/', details_game, name='details game'),
    path('game/delete/<int:pk>/', delete_game, name='delete game'),
    path('dashboard/', dashboard, name='dashboard'),
)

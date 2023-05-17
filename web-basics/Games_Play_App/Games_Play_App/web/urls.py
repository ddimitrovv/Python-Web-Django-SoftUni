from django.urls import path

from Games_Play_App.web.views import home_view, add_profile, create_game, dashboard, profile_details

urlpatterns = (
    path('', home_view, name='home'),
    path('profile/create', add_profile, name='add profile'),
    path('game/create', create_game, name='create game'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/details/', profile_details, name='profile details'),
)

# TODO:
# • http: // localhost: 8000 / - homepage
# • http: // localhost: 8000 / profile / create - createprofilepage - Done!
# • http: // localhost: 8000 / dashboard / - dashboardpage - Done!
# • http: // localhost: 8000 / game / create / - creategamepage Done!
# • http: // localhost: 8000 / game / details / < id > / - detailsgamepage
# • http: // localhost: 8000 / game / edit / < id > / - editgamepage
# • http: // localhost: 8000 / game / delete / < id > / - deletegamepage
# • http: // localhost: 8000 / profile / details / - detailsprofilepage
# • http: // localhost: 8000 / profile / edit / - editprofilepage
# • http: // localhost: 8000 / profile / delete / - deleteprofilepage

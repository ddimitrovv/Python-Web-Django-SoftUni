from django.urls import path, include

from My_Plant_App.web.views import home_view, add_profile, catalogue, create_plant, details_plant, profile_details

urlpatterns = (
    path('', home_view, name='home'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', add_profile, name='add profile'),
        path('details/', profile_details, name='profile details'),
    ])),
    path('create/', create_plant, name='create plant'),
    path('details/<int:pk>', details_plant, name='details plant'),
)

# TODO:

# • http: // localhost: 8000 / edit / < plant_id > / - plant edit page
# • http: // localhost: 8000 / delete / < plant_id > / - plant delete page

# • http: // localhost: 8000 / profile / edit / - profile edit page
# • http: // localhost: 8000 / profile / delete / - profile delete page

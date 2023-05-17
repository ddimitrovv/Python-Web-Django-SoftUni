from django.urls import path

from Games_Play_App.web.views import home_view, add_profile

urlpatterns = (
    path('', home_view, name='home'),
    path('profile/create', add_profile, name='add profile'),
)

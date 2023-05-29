from django.urls import path, include

from My_Music_app.web.views import home_view, profile_details, profile_delete

urlpatterns = (
    path('', home_view, name='home'),
    path('profile/', include([
        path('details/', profile_details, name='profile details'),
        path('delete/', profile_delete, name='profile delete'),
    ]))
)


# TODO:
# • http: // localhost: 8000 / album / add / - add album page
# • http: // localhost: 8000 / album / details / < id > / - album details page
# • http: // localhost: 8000 / album / edit / < id > / - edit album page
# • http: // localhost: 8000 / album / delete / < id > / - delete album page

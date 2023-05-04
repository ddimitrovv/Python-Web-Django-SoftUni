from django.urls import path

from Online_Library.web.views import home_view, add_book, profile_details, profile_edit, profile_delete

urlpatterns = (
    path('', home_view, name='home'),
    path('add/', add_book, name='add book'),
    path('profile/', profile_details, name='profile details'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete')
)


# TODO:
# • http: // localhost: 8000 / - home page - Done!
# • http: // localhost: 8000 / add / - add book page - Done!
# • http: // localhost: 8000 / edit /:id - edit book page
# • http: // localhost: 8000 / details /:id - book details page
# • http: // localhost: 8000 / profile / - profile page - Done!
# • http: // localhost: 8000 / profile / edit / - edit profile page - Done!
# • http: // localhost: 8000 / profile / delete / - delete profile page - Done!

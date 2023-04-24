from django.urls import path

from notes_app.web.views import index

urlpatterns = (
    path('', index, name='home-page'),
)

from django.contrib import admin

from notes_app.web.models import Profile, Note


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    ...


@admin.register(Note)
class AdminNote(admin.ModelAdmin):
    ...

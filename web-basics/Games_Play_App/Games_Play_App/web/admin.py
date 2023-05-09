from django.contrib import admin

from Games_Play_App.web.models import Profile, Game


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    ...

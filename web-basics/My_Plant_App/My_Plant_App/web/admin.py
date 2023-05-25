from django.contrib import admin

from My_Plant_App.web.models import Profile, Plant


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    ...

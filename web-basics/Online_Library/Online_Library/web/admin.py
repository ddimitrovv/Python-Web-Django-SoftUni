from django.contrib import admin

from Online_Library.web.models import Profile, Book


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ...

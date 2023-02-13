from django.contrib import admin

from Python_Web_Basics_Exam_01_November_2020.recipes.models import Recipe


@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    pass

from django import forms

from Python_Web_Basics_Exam_01_November_2020.recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

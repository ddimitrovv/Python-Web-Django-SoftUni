from django.shortcuts import render

from Python_Web_Basics_Exam_01_November_2020.recipes.forms import RecipeForm


# Create your views here.
def index(request):
    if request.method == 'GET':
        form = RecipeForm
    if request.method == 'POST':
        form = RecipeForm(request.POST or None)
    return render(request, 'index.html', {'form': form})

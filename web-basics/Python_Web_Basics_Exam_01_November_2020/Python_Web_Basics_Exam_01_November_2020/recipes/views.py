from django.shortcuts import render, redirect

from Python_Web_Basics_Exam_01_November_2020.recipes.forms import RecipeForm
from Python_Web_Basics_Exam_01_November_2020.recipes.models import Recipe


# Create your views here.
def index(request):
    form = Recipe.objects.all()
    return render(request, 'index.html', {'form': form})


def create_recipe(request):
    if request.method == 'GET':
        form = RecipeForm()
    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main-page')

    context = {
        'form': form,
    }

    return render(
        request,
        'index.html',
        context,
    )


def edit_recipe(request, pk):
    recipe = Recipe.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('main-page')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(
        request,
        'edit.html',
        context,
    )


def details_recipe(request, pk):
    recipe = Recipe.objects \
        .filter(pk=pk) \
        .get()

    context = {
        'recipe': recipe,
    }

    return render(
        request,
        'details.html',
        context,
    )


def delete_recipe(request, pk):
    recipe = Recipe.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('main-page')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(
        request,
        'delete.html',
        context,
    )

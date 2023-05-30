from http.client import HTTPResponse

from django.http import Http404
from django.shortcuts import render, redirect

from Recipes.web.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from Recipes.web.models import Recipe


def get_recipe(pk):
    recipe = Recipe.objects.filter(id=pk).get()
    return recipe


def home_view(request):
    recipes = Recipe.objects.all() or None
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'GET':
        form = RecipeCreateForm()
    else:
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def details_recipe(request, pk):
    recipe = get_recipe(pk)
    ingredients = recipe.ingredients.split(',')
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'details.html', context)


def edit_recipe(request, pk):
    recipe = get_recipe(pk)
    if request.method == 'GET':
        form = RecipeEditForm(instance=recipe)
    else:
        form = RecipeEditForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = get_recipe(pk)
    if request.method == 'GET':
        form = RecipeDeleteForm(instance=recipe)
    else:
        form = RecipeDeleteForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'delete.html', context)

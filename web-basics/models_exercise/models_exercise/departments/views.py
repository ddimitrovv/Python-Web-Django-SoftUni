from django.shortcuts import render

from models_exercise.departments.forms import NameForm
from models_exercise.departments.models import Departments


def show_all_departments(request):
    all_departments = Departments.objects.all()
    context = {'departments': all_departments}
    return render(request, 'departments.html', context)


def add_new_name(request):
    if request.method == 'GET':
        form = NameForm
    if request.method == 'POST':
        form = NameForm(request.POST or None)
        if form.is_valid():
            form.save()

    return render(request, 'index.html', {'form': form})

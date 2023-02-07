from django.shortcuts import render

from models_exercise.departments.models import Departments


def show_all_departments(request):
    all_departments = Departments.objects.all()
    context = {'departments': all_departments}
    return render(request, 'departments.html', context)

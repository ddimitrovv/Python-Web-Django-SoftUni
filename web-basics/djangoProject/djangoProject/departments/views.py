from django.http import HttpResponse
from django.shortcuts import render

from djangoProject.departments.models import Departments


def show_department(request):
    return HttpResponse('Department Details Page')


def show_department_by_id(request, department_id):
    # if department_id == 1:
    #     department_name = 'Developers'
    # elif department_id == 2:
    #     department_name = 'Trainers'

    department = Departments.objects.get(id=department_id)

    html = (f'<html><body><h1> Department Name: {department.name},'
            f' Department ID: {department.pk} <h1><body><html>')

    return HttpResponse(html)

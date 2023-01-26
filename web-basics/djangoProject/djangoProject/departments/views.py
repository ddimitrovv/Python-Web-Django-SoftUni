from django.http import HttpResponse, Http404
from django.shortcuts import render

from djangoProject.departments.models import Departments


def show_department(request):
    return HttpResponse('Department Details Page')


# def show_department_by_id(request, department_id):
#     department_name = ''

#     if department_id == 1:
#         department_name = 'Developers'
#     elif department_id == 2:
#         department_name = 'Trainers'
#
#     html = f'<html><body><h1> Department Name: {department_name},' \
#            f' Department ID: {department_id} <h1><body><html>'
#
#     return HttpResponse(html)


# def show_department_by_id(request, department_id):
#     department = Departments.objects.get(id=department_id)
#     context = {
#         'department_name': department.name,
#         'department_id': department.pk
#     }
#
#     return render(
#         request=request,
#         template_name='tasks/department-details.html',
#         context=context
#     )


def show_department_by_id(request, department_id):
    department = Departments.objects.filter(id=department_id)
    if department:
        department = department.get()
        context = {
            'department_name': department.name,
            'department_id': department.pk
        }
        return render(request, 'tasks/department-details.html', context)
    else:
        raise Http404

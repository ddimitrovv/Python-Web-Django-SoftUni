from django.shortcuts import render

from djangoProject.employee.models import Employee


def employee_info(request):
    employees = Employee.objects.all()

    context = {'employees': employees}

    return render(request, 'tasks/employees-info.html', context)

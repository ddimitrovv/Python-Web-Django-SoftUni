from django.shortcuts import render

from models_exercise.employees.forms import EmployeeForm
from models_exercise.employees.models import Employee


def add_new_employee(request):
    if request.method == 'GET':
        form = EmployeeForm
    if request.method == 'POST':
        form = EmployeeForm(request.POST or None)
        if form.is_valid():
            employee = Employee(request)
            form.save(employee)

    return render(request, 'add-employee.html', {'form': form})


def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
    return render(request, 'update-employee.html', {'form': form})

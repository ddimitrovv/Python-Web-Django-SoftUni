from django import forms

from models_exercise.employees.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email_address': 'Email',
            'works_full_time': 'Works full time',
            'month_of_employment': 'Month of employment',
            'job_level': 'Job level',
            'photo': 'Photo',
            'birth_date': 'Date of birth',
            'department': 'Department',
            'year_of_employment': 'Year of employment'
        }
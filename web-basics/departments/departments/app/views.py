from django.http import HttpResponse
from django.shortcuts import render


def show_department(request):
    return HttpResponse("Department Details Page")

from django.shortcuts import render
from django.http import JsonResponse
# from rest_framework.renderers import JSONResponse
from employeesmanagement.employeeslist.serializer import employeeSerializer
from employeesmanagement.employeeslist.models import employee


def employeeslist(request):
    if request.method == 'GET':
        employees = employee.objects.all()
        serializer = employeeSerializer(employees)
        return JsonResponse(serializer.data)
from django.shortcuts import render
from django.http import JsonResponse
# from rest_framework.renderers import JSONResponse
from employeesmanagement.employeeslist.serializer import employeeSerializer
from employeesmanagement.employeeslist.models import employee 
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status


class EmployeesListViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

    
@api_view( ['GET', 'POST', 'DELETE'])
def employeeslist(request):
    if request.method == 'GET':
        employees = employee.objects.all()
        serializer = employeeSerializer(employees)
        return JsonResponse(serializer.data)
    

    elif request.method == 'PUT': 
        current_data = JSONParser().parse(request) 
        current_serializer = employeeSerializer(employee, data=current_data) 
        current_serializer.save() 
        return JsonResponse(current_serializer.data)
    
    
    elif request.method == 'POST':
        current_data = JSONParser().parse(request)
        current_serializer = employeeSerializer(data=current_data)
        if current_serializer.is_valid():
            current_serializer.save()
            return JsonResponse(current_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(current_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
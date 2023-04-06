from django.shortcuts import render
from django.http import HttpResponse

def employeeslist(request):
    if request.method == 'GET':
        return HttpResponse('ok!')
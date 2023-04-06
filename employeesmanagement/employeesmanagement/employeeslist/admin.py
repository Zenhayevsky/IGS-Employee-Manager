from django.contrib import admin
from employeesmanagement.employeeslist.models import employee


class EmployeeAdmmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    list_filter = ('department',)


admin.site.register(employee, EmployeeAdmmin)

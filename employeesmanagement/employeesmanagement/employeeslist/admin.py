from django.contrib import admin
from employeesmanagement.employeeslist.models import employee, Department


class EmployeeAdmmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    list_filter = ('department',)

class DepartmentAdmmin(admin.ModelAdmin):
    list_display = ('namedepartment',)

admin.site.register(employee, EmployeeAdmmin)
admin.site.register(Department, DepartmentAdmmin)

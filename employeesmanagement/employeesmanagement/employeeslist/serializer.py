from rest_framework import serializers
from employeesmanagement.employeeslist.models import employee


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ['id', 'name', 'email', 'department']
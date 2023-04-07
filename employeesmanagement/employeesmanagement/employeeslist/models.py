from django.db import models


class employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    department = models.OneToOneField('Department', on_delete=models.SET('6'))


    class Meta: 
        db_table = 'employeesMn'

    def __str__(self):
        return self.name
    
class Department(models.Model): 
    namedepartment = models.CharField(max_length=255)

    def __str__(self):
        return self.namedepartment
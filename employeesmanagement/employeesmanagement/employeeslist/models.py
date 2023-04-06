from django.db import models


class employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    class Meta: 
        db_table = 'employeesM'

    def __str__(self):
        return self.name
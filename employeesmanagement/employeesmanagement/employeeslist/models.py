from django.db import models


class employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
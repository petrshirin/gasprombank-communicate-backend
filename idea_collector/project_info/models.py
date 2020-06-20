from django.db import models

# Create your models here.


class Technology(models.Model):
    name = models.CharField(max_length=255)


class Block(models.Model):
    name = models.CharField(max_length=255)


class Function(models.Model):
    name = models.CharField(max_length=255)


class Department(models.Model):
    name = models.CharField(max_length=200)


class Position(models.Model):
    name = models.CharField(max_length=255)
    departament = models.ForeignKey(Department, on_delete=models.CASCADE)